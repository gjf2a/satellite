from satellite import *
from pyhop_anytime import *


def start(state, goals):
    tasks = [[('plan_photo', target, mode), ('start', goals)]
             for target, mode in goals.have_image if not state.have_image.get((target,mode), False)]
    if len(tasks) > 0:
        return TaskList(tasks)
    else:
        pointings = get_pointings(state)
        tasks = [[('turn_to', satellite, target, pointings[satellite]), ('start', goals)]
                 for satellite, target in goals.pointing if not state.pointing.get((satellite, target), False)]
        if len(tasks) > 0:
            return TaskList(tasks)
        else:
            return TaskList(completed=True)


def get_pointings(state):
    return {satellite: target for ((satellite, target), t) in state.pointing.items()}


def plan_photo(state, target, mode):
    instruments = {i for ((i, m), t) in state.supports.items() if t and m == mode}
    satellites = [(s, i) for ((i, s), t) in state.on_board.items() if t and i in instruments]
    return TaskList([[('set_up', s, i, target), ('take_image', s, target, i, mode)] for s, i in satellites])


def set_up(state, satellite, instrument, target):
    tasks = []
    if not state.calibrated.get(instrument, False):
        tasks.append(('find_calibrator_for', satellite, instrument))
    tasks.append(('activate', satellite, instrument, target))
    print("***set_up tasks:", tasks)
    return TaskList(tasks)


def find_calibrator_for(state, satellite, instrument):
    result = TaskList([[('activate', satellite, instrument, d), ('calibrate', satellite, instrument, d)]
                       for ((i, d), t) in state.calibration_target.items() if instrument == i])
    print("***calibrator tasks:", result)
    return result


def activate(state, satellite, instrument, target):
    tasks = []
    if not state.pointing.get((satellite, target), False):
        pointings = get_pointings(state)
        tasks.append(('turn_to', satellite, target, pointings[satellite]))
    if not state.power_on.get(instrument, False):
        if not state.power_avail.get(satellite, False):
            already_on = [i for ((i, s), t) in state.on_board.items() if state.power_on.get(i, False) and s == satellite]
            tasks.append(('switch_off', already_on[0], satellite))
        tasks.append(('switch_on', instrument, satellite))
    return TaskList(tasks, completed=True)


def make_satellite_planner():
    planner = Planner()
    planner.declare_operators(calibrate, switch_off, switch_on, take_image, turn_to)
    planner.declare_methods('start', start)
    planner.declare_methods('plan_photo', plan_photo)
    planner.declare_methods('set_up', set_up)
    planner.declare_methods('find_calibrator_for', find_calibrator_for)
    planner.declare_methods('activate', activate)
    return planner


if __name__ == '__main__':
    from strips_sat_x_1_0 import *
    planner = make_satellite_planner()
    plans = planner.anyhop(strips_sat_x_1_state, [('start', strips_sat_x_1_goals)], verbose=3)
    print(plans)