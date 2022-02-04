from pyhop_anytime import *

strips_sat_x_1_state = State('strips_sat_x_1_state')
strips_sat_x_1_state.calibration_target = {('instrument0','groundstation2'):True}
strips_sat_x_1_state.on_board = {('instrument0','satellite0'):True}
strips_sat_x_1_state.pointing = {('satellite0','phenomenon6'):True}
strips_sat_x_1_state.power_avail = {'satellite0':True}
strips_sat_x_1_state.supports = {('instrument0','thermograph0'):True}
strips_sat_x_1_state.calibrated = {}
strips_sat_x_1_state.have_image = {}
strips_sat_x_1_state.power_on = {}

strips_sat_x_1_goals = State('strips_sat_x_1_goals')
strips_sat_x_1_goals.have_image = {('phenomenon4','thermograph0'):True,('phenomenon6','thermograph0'):True,('star5','thermograph0'):True}

