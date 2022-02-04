from pyhop_anytime import *

strips_sat_x_1_state = State('strips_sat_x_1_state')
strips_sat_x_1_state.calibration_target = {('instrument0','star0'):True,('instrument1','groundstation2'):True}
strips_sat_x_1_state.on_board = {('instrument0','satellite0'):True,('instrument1','satellite0'):True}
strips_sat_x_1_state.pointing = {('satellite0','planet4'):True}
strips_sat_x_1_state.power_avail = {'satellite0':True}
strips_sat_x_1_state.supports = {('instrument0','infrared0'):True,('instrument0','infrared1'):True,('instrument1','image2'):True,('instrument1','infrared0'):True,('instrument1','infrared1'):True}
strips_sat_x_1_state.calibrated = {}
strips_sat_x_1_state.have_image = {}
strips_sat_x_1_state.power_on = {}

strips_sat_x_1_goals = State('strips_sat_x_1_goals')
strips_sat_x_1_goals.have_image = {('phenomenon5','image2'):True,('phenomenon6','infrared0'):True,('planet3','infrared0'):True,('planet4','infrared0'):True,('star7','infrared0'):True}

