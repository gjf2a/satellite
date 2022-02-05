from pyhop_anytime import *

strips_sat_x_1_state = State('strips_sat_x_1_state')
strips_sat_x_1_state.calibration_target = Oset([('instrument0','star1'),('instrument1','groundstation0'),('instrument2','groundstation2'),('instrument3','groundstation4'),('instrument4','star1'),('instrument5','star1'),('instrument6','groundstation4'),('instrument7','groundstation0')])
strips_sat_x_1_state.on_board = Oset([('instrument0','satellite0'),('instrument1','satellite0'),('instrument2','satellite0'),('instrument3','satellite1'),('instrument4','satellite2'),('instrument5','satellite2'),('instrument6','satellite3'),('instrument7','satellite3')])
strips_sat_x_1_state.pointing = Oset([('satellite0','star6'),('satellite1','groundstation0'),('satellite2','star6'),('satellite3','groundstation2')])
strips_sat_x_1_state.power_avail = Oset(['satellite0','satellite1','satellite2','satellite3'])
strips_sat_x_1_state.supports = Oset([('instrument0','image1'),('instrument0','image3'),('instrument1','image3'),('instrument2','image0'),('instrument3','image0'),('instrument3','image2'),('instrument4','image0'),('instrument4','image1'),('instrument5','image0'),('instrument5','image1'),('instrument5','image2'),('instrument6','image0'),('instrument6','image1'),('instrument6','image2'),('instrument7','image0'),('instrument7','image1'),('instrument7','image3')])
strips_sat_x_1_state.calibrated = Oset()
strips_sat_x_1_state.have_image = Oset()
strips_sat_x_1_state.power_on = Oset()

strips_sat_x_1_goals = State('strips_sat_x_1_goals')
strips_sat_x_1_goals.have_image = Oset([('phenomenon5','image0'),('planet10','image0'),('planet11','image2'),('planet8','image0'),('planet9','image3'),('star6','image1'),('star7','image0')])
strips_sat_x_1_goals.pointing = Oset([('satellite1','star1'),('satellite2','phenomenon5')])

