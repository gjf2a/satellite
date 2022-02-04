def calibrate(state, s, i, d):
    if state.on_board.get((i,s), False) and state.calibration_target.get((i,d), False) and state.pointing.get((s,d), False) and state.power_on.get(i, False):
        state.calibrated[i] = True
        return state


def switch_off(state, i, s):
    if state.on_board.get((i,s), False) and state.power_on.get(i, False):
        state.power_on[i] = False
        state.power_avail[s] = True
        return state


def switch_on(state, i, s):
    if state.on_board.get((i,s), False) and state.power_avail.get(s, False):
        state.power_on[i] = True
        state.calibrated[i] = False
        state.power_avail[s] = False
        return state


def take_image(state, s, d, i, m):
    if state.calibrated.get(i, False) and state.on_board.get((i,s), False) and state.supports.get((i,m), False) and state.power_on.get(i, False) and state.pointing.get((s,d), False) and state.power_on.get(i, False):
        state.have_image[(d,m)] = True
        return state


def turn_to(state, s, d_new, d_prev):
    if state.pointing.get((s,d_prev), False) and d_new != d_prev:
        state.pointing[(s,d_new)] = True
        state.pointing[(s,d_prev)] = False
        return state


