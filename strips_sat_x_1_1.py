from pyhop_anytime import *

strips_sat_x_1_state = State('strips_sat_x_1_state')
strips_sat_x_1_state.calibration_target = {('instrument0','star0'),('instrument1','star2'),('instrument2','star2')}
strips_sat_x_1_state.on_board = {('instrument0','satellite0'),('instrument1','satellite1'),('instrument2','satellite1')}
strips_sat_x_1_state.pointing = {('satellite0','star6'),('satellite1','star0')}
strips_sat_x_1_state.power_avail = {'satellite0','satellite1'}
strips_sat_x_1_state.supports = {('instrument0','infrared0'),('instrument0','thermograph2'),('instrument1','infrared0'),('instrument1','infrared1'),('instrument1','thermograph2'),('instrument2','infrared1'),('instrument2','thermograph2')}
strips_sat_x_1_state.calibrated = set()
strips_sat_x_1_state.have_image = set()
strips_sat_x_1_state.power_on = set()

strips_sat_x_1_goals = State('strips_sat_x_1_goals')
strips_sat_x_1_goals.have_image = {('phenomenon8','thermograph2'),('phenomenon9','infrared0'),('planet3','infrared1'),('planet5','thermograph2'),('star4','infrared1'),('star6','infrared1'),('star7','infrared0')}
strips_sat_x_1_goals.pointing = {('satellite1','planet5')}

