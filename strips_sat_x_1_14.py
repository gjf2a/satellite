from pyhop_anytime import *

strips_sat_x_1_state = State('strips_sat_x_1_state')
strips_sat_x_1_state.calibration_target = {('instrument0','star1'),('instrument1','star2'),('instrument2','star2'),('instrument3','star2'),('instrument4','star0')}
strips_sat_x_1_state.on_board = {('instrument0','satellite0'),('instrument1','satellite1'),('instrument2','satellite1'),('instrument3','satellite1'),('instrument4','satellite2')}
strips_sat_x_1_state.pointing = {('satellite0','phenomenon8'),('satellite1','star6'),('satellite2','star6')}
strips_sat_x_1_state.power_avail = {'satellite0','satellite1','satellite2'}
strips_sat_x_1_state.supports = {('instrument0','infrared1'),('instrument0','spectrograph0'),('instrument1','infrared3'),('instrument2','infrared1'),('instrument2','infrared3'),('instrument2','thermograph2'),('instrument3','infrared1'),('instrument3','infrared3'),('instrument3','spectrograph0'),('instrument4','infrared3')}
strips_sat_x_1_state.calibrated = set()
strips_sat_x_1_state.have_image = set()
strips_sat_x_1_state.power_on = set()

strips_sat_x_1_goals = State('strips_sat_x_1_goals')
strips_sat_x_1_goals.have_image = {('phenomenon8','spectrograph0'),('planet4','thermograph2'),('planet5','spectrograph0'),('star10','infrared3'),('star6','thermograph2'),('star7','infrared3'),('star9','infrared1')}

