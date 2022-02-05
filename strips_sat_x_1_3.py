from pyhop_anytime import *

strips_sat_x_1_state = State('strips_sat_x_1_state')
strips_sat_x_1_state.calibration_target = {('instrument0','star0'),('instrument1','groundstation2')}
strips_sat_x_1_state.on_board = {('instrument0','satellite0'),('instrument1','satellite0')}
strips_sat_x_1_state.pointing = {('satellite0','planet4')}
strips_sat_x_1_state.power_avail = {'satellite0'}
strips_sat_x_1_state.supports = {('instrument0','infrared0'),('instrument0','infrared1'),('instrument1','image2'),('instrument1','infrared0'),('instrument1','infrared1')}
strips_sat_x_1_state.calibrated = set()
strips_sat_x_1_state.have_image = set()
strips_sat_x_1_state.power_on = set()

strips_sat_x_1_goals = State('strips_sat_x_1_goals')
strips_sat_x_1_goals.have_image = {('phenomenon5','image2'),('phenomenon6','infrared0'),('planet3','infrared0'),('planet4','infrared0'),('star7','infrared0')}

