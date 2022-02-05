from pyhop_anytime import *

strips_sat_x_1_state = State('strips_sat_x_1_state')
strips_sat_x_1_state.calibration_target = {('instrument0','groundstation2')}
strips_sat_x_1_state.on_board = {('instrument0','satellite0')}
strips_sat_x_1_state.pointing = {('satellite0','phenomenon6')}
strips_sat_x_1_state.power_avail = {'satellite0'}
strips_sat_x_1_state.supports = {('instrument0','thermograph0')}
strips_sat_x_1_state.calibrated = set()
strips_sat_x_1_state.have_image = set()
strips_sat_x_1_state.power_on = set()

strips_sat_x_1_goals = State('strips_sat_x_1_goals')
strips_sat_x_1_goals.have_image = {('phenomenon4','thermograph0'),('phenomenon6','thermograph0'),('star5','thermograph0')}

