from pyhop_anytime import *

strips_sat_x_1_state = State('strips_sat_x_1_state')
strips_sat_x_1_state.calibration_target = Oset([('instrument0','star0'),('instrument1','star2'),('instrument2','star2')])
strips_sat_x_1_state.on_board = Oset([('instrument0','satellite0'),('instrument1','satellite1'),('instrument2','satellite1')])
strips_sat_x_1_state.pointing = Oset([('satellite0','star6'),('satellite1','star0')])
strips_sat_x_1_state.power_avail = Oset(['satellite0','satellite1'])
strips_sat_x_1_state.supports = Oset([('instrument0','infrared0'),('instrument0','thermograph2'),('instrument1','infrared0'),('instrument1','infrared1'),('instrument1','thermograph2'),('instrument2','infrared1'),('instrument2','thermograph2')])
strips_sat_x_1_state.calibrated = Oset()
strips_sat_x_1_state.have_image = Oset()
strips_sat_x_1_state.power_on = Oset()

strips_sat_x_1_goals = State('strips_sat_x_1_goals')
strips_sat_x_1_goals.have_image = Oset([('phenomenon8','thermograph2'),('phenomenon9','infrared0'),('planet3','infrared1'),('planet5','thermograph2'),('star4','infrared1'),('star6','infrared1'),('star7','infrared0')])
strips_sat_x_1_goals.pointing = Oset([('satellite1','planet5')])

