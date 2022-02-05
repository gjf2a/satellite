# Solves: 0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19
# More than one plan in 1 second: 1(2), 5 (2), 8 (2), 11 (2), 12 (3), 14 (3)
# Does not solve: 6, 17

from satellite import *
from pyhop_anytime import *
import sys


def start(state, goals):
    tasks = [[('plan_photo', target, mode), ('start', goals)]
             for target, mode in goals.have_image if not state.have_image.get((target,mode), False)]
    if len(tasks) > 0:
        return TaskList(tasks)
    else:
        pointings = get_pointings(state)
        if hasattr(goals, 'pointing'):
            tasks = [[('turn_to', satellite, target, pointings[satellite]), ('start', goals)]
                     for satellite, target in goals.pointing if not state.pointing.get((satellite, target), False)]
        if len(tasks) > 0:
            return TaskList(tasks)
        else:
            return TaskList(completed=True)


def get_pointings(state):
    return {satellite: target for ((satellite, target), t) in state.pointing.items() if t}


def plan_photo(state, target, mode):
    instruments = {i for ((i, m), t) in state.supports.items() if t and m == mode}
    satellites = [(s, i) for ((i, s), t) in state.on_board.items() if t and i in instruments]
    return TaskList([[('set_up', s, i, target), ('take_image', s, target, i, mode)] for s, i in satellites])


def set_up(state, satellite, instrument, target):
    tasks = []
    if not state.calibrated.get(instrument, False):
        tasks.append(('find_calibrator_for', satellite, instrument))
    tasks.append(('activate', satellite, instrument, target))
    return TaskList(tasks)


def find_calibrator_for(state, satellite, instrument):
    return TaskList([[('activate', satellite, instrument, d), ('calibrate', satellite, instrument, d)]
                     for ((i, d), t) in state.calibration_target.items() if t and instrument == i])


def activate(state, satellite, instrument, target):
    tasks = []
    if not state.pointing.get((satellite, target), False):
        pointings = get_pointings(state)
        tasks.append(('turn_to', satellite, target, pointings[satellite]))
    if not state.power_on.get(instrument, False):
        if not state.power_avail.get(satellite, False):
            already_on = [i for ((i, s), t) in state.on_board.items() if t and state.power_on.get(i, False) and s == satellite]
            tasks.append(('switch_off', already_on[0], satellite))
        tasks.append(('switch_on', instrument, satellite))
    return TaskList(tasks, completed=True)


def turn(state, s, d_new):
    d_prev = [d for ((s1, d), t) in state.pointing.items() if t and s1 == s]
    if state.pointing.get((s,d_prev), False) and d_new != d_prev:
        state.pointing[(s,d_new)] = True
        state.pointing[(s,d_prev)] = False
        return state


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
    if len(sys.argv) == 1:
        print("Usage: python3 satellite_planner.py -v:[verbosity] -s:[max seconds] [planner_file]+")
    else:
        verbosity = 1
        max_seconds = None
        for filename in sys.argv[1:]:
            if filename.startswith("-v"):
                verbosity = int(filename.split(':')[1])
            elif filename.startswith("-s"):
                max_seconds = float(filename.split(':')[1])
            else:
                exec(f"from {filename} import *")
                planner = make_satellite_planner()
                plans = planner.anyhop(strips_sat_x_1_state, [('start', strips_sat_x_1_goals)], max_seconds=max_seconds, verbose=verbosity)
                for (plan, time) in plans:
                    print(plan)
                for (plan, time) in plans:
                    print(f"Length: {len(plan)} time: {time}")
                print(len(plans), "total plans generated")