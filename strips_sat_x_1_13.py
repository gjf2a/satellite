from pyhop_anytime import *

strips_sat_x_1_state = State('strips_sat_x_1_state')
strips_sat_x_1_state.calibration_target = Oset([('instrument0','groundstation2')])
strips_sat_x_1_state.on_board = Oset([('instrument0','satellite0')])
strips_sat_x_1_state.pointing = Oset([('satellite0','phenomenon6')])
strips_sat_x_1_state.power_avail = Oset(['satellite0'])
strips_sat_x_1_state.supports = Oset([('instrument0','thermograph0')])
strips_sat_x_1_state.calibrated = Oset()
strips_sat_x_1_state.have_image = Oset()
strips_sat_x_1_state.power_on = Oset()

strips_sat_x_1_goals = State('strips_sat_x_1_goals')
strips_sat_x_1_goals.have_image = Oset([('phenomenon4','thermograph0'),('phenomenon6','thermograph0'),('star5','thermograph0')])

