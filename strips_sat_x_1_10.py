from pyhop_anytime import *

strips_sat_x_1_state = State('strips_sat_x_1_state')
strips_sat_x_1_state.calibration_target = {('instrument0','star1'),('instrument1','groundstation3'),('instrument10','star0'),('instrument2','groundstation3'),('instrument3','star4'),('instrument4','star2'),('instrument5','star0'),('instrument6','groundstation3'),('instrument7','star4'),('instrument8','star4'),('instrument9','star2')}
strips_sat_x_1_state.on_board = {('instrument0','satellite0'),('instrument1','satellite0'),('instrument10','satellite4'),('instrument2','satellite1'),('instrument3','satellite1'),('instrument4','satellite2'),('instrument5','satellite2'),('instrument6','satellite3'),('instrument7','satellite3'),('instrument8','satellite4'),('instrument9','satellite4')}
strips_sat_x_1_state.pointing = {('satellite0','star0'),('satellite1','star4'),('satellite2','star1'),('satellite3','groundstation3'),('satellite4','planet10')}
strips_sat_x_1_state.power_avail = {'satellite0','satellite1','satellite2','satellite3','satellite4'}
strips_sat_x_1_state.supports = {('instrument0','image4'),('instrument1','infrared0'),('instrument1','spectrograph1'),('instrument10','image2'),('instrument10','image4'),('instrument2','image2'),('instrument2','infrared0'),('instrument3','infrared0'),('instrument3','infrared3'),('instrument4','image4'),('instrument4','infrared0'),('instrument4','spectrograph1'),('instrument5','image2'),('instrument5','infrared0'),('instrument5','infrared3'),('instrument6','infrared0'),('instrument6','infrared3'),('instrument7','image4'),('instrument7','infrared3'),('instrument7','spectrograph1'),('instrument8','image4'),('instrument8','spectrograph1'),('instrument9','infrared3')}
strips_sat_x_1_state.calibrated = set()
strips_sat_x_1_state.have_image = set()
strips_sat_x_1_state.power_on = set()

strips_sat_x_1_goals = State('strips_sat_x_1_goals')
strips_sat_x_1_goals.have_image = {('phenomenon13','image4'),('phenomenon14','spectrograph1'),('phenomenon8','image4'),('planet10','infrared3'),('planet5','image4'),('planet9','infrared0'),('star12','image4'),('star15','spectrograph1'),('star16','image2'),('star6','infrared3'),('star7','image4')}
strips_sat_x_1_goals.pointing = {('satellite4','planet9')}

