# Solves: All
# More than one plan in 1 second: 1 (4), 5 (2), 6 (3), 7 (3), 8 (4), 10 (3), 11 (2), 12 (4), 14 (6), 16 (2), 17 (3), 18 (2)
# Even more plans with 3 seconds: 1 (7)

from satellite.satellite import *
from pyhop_anytime import *


def start(state, goals):
    tasks = [[('plan_photo', target, mode), ('start', goals)]
             for target, mode in goals.have_image if (target,mode) not in state.have_image]
    if len(tasks) > 0:
        return TaskList(tasks)
    else:
        pointings = get_pointings(state)
        if hasattr(goals, 'pointing'):
            tasks = [[('turn_to', satellite, target, pointings[satellite]), ('start', goals)]
                     for satellite, target in goals.pointing if (satellite, target) not in state.pointing]
        if len(tasks) > 0:
            return TaskList(tasks)
        else:
            return TaskList(completed=True)


def get_pointings(state):
    return {satellite: target for (satellite, target) in state.pointing}


def plan_photo(state, target, mode):
    instruments = {i for (i, m) in state.supports if m == mode}
    satellites = [(s, i) for i, s in state.on_board if i in instruments]
    return TaskList([[('set_up', s, i, target), ('take_image', s, target, i, mode)] for s, i in satellites])


def set_up(state, satellite, instrument, target):
    return TaskList([('find_calibrator_for', satellite, instrument), ('aim', satellite, target)])


def aim(state, satellite, target):
    tasks = []
    if (satellite, target) not in state.pointing:
        pointings = get_pointings(state)
        tasks.append(('turn_to', satellite, target, pointings[satellite]))
    return TaskList(tasks, completed=True)


def find_calibrator_for(state, satellite, instrument):
    if instrument in state.calibrated and instrument in state.power_on:
        return TaskList(completed=True)
    else:
        return TaskList([[('activate', satellite, instrument, d), ('calibrate', satellite, instrument, d)]
                         for i, d in state.calibration_target if instrument == i])


def activate(state, satellite, instrument, target):
    tasks = [('aim', satellite, target)]
    if instrument not in state.power_on:
        if satellite not in state.power_avail:
            already_on = [i for i, s in state.on_board if i in state.power_on and s == satellite]
            tasks.append(('switch_off', already_on[0], satellite))
        tasks.append(('switch_on', instrument, satellite))
    return TaskList(tasks, completed=True)


def make_satellite_planner():
    planner = Planner()
    planner.declare_operators(calibrate, switch_off, switch_on, take_image, turn_to)
    planner.declare_methods(start, plan_photo, set_up, find_calibrator_for, activate, aim)
    return planner


if __name__ == '__main__':
    #anyhop_main(make_satellite_planner())
    anyhop_args(make_satellite_planner(), ["strips_sat_x_1_17.py", "-s:2"])
