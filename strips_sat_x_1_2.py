from pyhop_anytime import *

strips_sat_x_1_state = State('strips_sat_x_1_state')
strips_sat_x_1_state.calibration_target = Oset([('instrument0','groundstation2'),('instrument1','groundstation1'),('instrument2','groundstation0'),('instrument3','groundstation0'),('instrument4','groundstation2'),('instrument5','groundstation1'),('instrument6','groundstation1'),('instrument7','groundstation1'),('instrument8','groundstation0')])
strips_sat_x_1_state.on_board = Oset([('instrument0','satellite0'),('instrument1','satellite0'),('instrument2','satellite0'),('instrument3','satellite1'),('instrument4','satellite1'),('instrument5','satellite1'),('instrument6','satellite2'),('instrument7','satellite2'),('instrument8','satellite2')])
strips_sat_x_1_state.pointing = Oset([('satellite0','phenomenon8'),('satellite1','groundstation2'),('satellite2','phenomenon5')])
strips_sat_x_1_state.power_avail = Oset(['satellite0','satellite1','satellite2'])
strips_sat_x_1_state.supports = Oset([('instrument0','image2'),('instrument0','spectrograph1'),('instrument0','thermograph0'),('instrument1','image2'),('instrument1','spectrograph1'),('instrument1','thermograph0'),('instrument2','image2'),('instrument3','spectrograph1'),('instrument3','thermograph0'),('instrument4','image2'),('instrument4','spectrograph1'),('instrument5','image2'),('instrument5','spectrograph1'),('instrument5','thermograph0'),('instrument6','image2'),('instrument7','image2'),('instrument7','thermograph0'),('instrument8','image2'),('instrument8','spectrograph1'),('instrument8','thermograph0')])
strips_sat_x_1_state.calibrated = Oset()
strips_sat_x_1_state.have_image = Oset()
strips_sat_x_1_state.power_on = Oset()

strips_sat_x_1_goals = State('strips_sat_x_1_goals')
strips_sat_x_1_goals.have_image = Oset([('phenomenon5','image2'),('phenomenon6','image2'),('phenomenon8','image2'),('planet9','spectrograph1'),('star3','thermograph0'),('star7','thermograph0')])
strips_sat_x_1_goals.pointing = Oset([('satellite0','phenomenon5'),('satellite1','groundstation2')])

