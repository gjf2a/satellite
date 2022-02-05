from pyhop_anytime import *

strips_sat_x_1_state = State('strips_sat_x_1_state')
strips_sat_x_1_state.calibration_target = {('instrument0','groundstation2'),('instrument1','groundstation0'),('instrument10','groundstation0'),('instrument11','groundstation1'),('instrument2','groundstation2'),('instrument3','groundstation2'),('instrument4','groundstation1'),('instrument5','groundstation4'),('instrument6','groundstation0'),('instrument7','groundstation4'),('instrument8','groundstation2'),('instrument9','groundstation2')}
strips_sat_x_1_state.on_board = {('instrument0','satellite0'),('instrument1','satellite0'),('instrument10','satellite4'),('instrument11','satellite5'),('instrument2','satellite0'),('instrument3','satellite1'),('instrument4','satellite2'),('instrument5','satellite2'),('instrument6','satellite2'),('instrument7','satellite3'),('instrument8','satellite3'),('instrument9','satellite4')}
strips_sat_x_1_state.pointing = {('satellite0','phenomenon12'),('satellite1','groundstation1'),('satellite2','groundstation2'),('satellite3','groundstation4'),('satellite4','planet15'),('satellite5','phenomenon11')}
strips_sat_x_1_state.power_avail = {'satellite0','satellite1','satellite2','satellite3','satellite4','satellite5'}
strips_sat_x_1_state.supports = {('instrument0','image1'),('instrument0','thermograph0'),('instrument1','image2'),('instrument1','thermograph3'),('instrument10','image1'),('instrument10','thermograph3'),('instrument11','image2'),('instrument11','thermograph0'),('instrument2','image1'),('instrument2','thermograph3'),('instrument2','thermograph4'),('instrument3','image2'),('instrument3','thermograph0'),('instrument3','thermograph4'),('instrument4','image1'),('instrument4','thermograph0'),('instrument4','thermograph4'),('instrument5','thermograph4'),('instrument6','image1'),('instrument6','thermograph3'),('instrument7','image2'),('instrument7','thermograph3'),('instrument8','thermograph0'),('instrument8','thermograph4'),('instrument9','image1'),('instrument9','image2'),('instrument9','thermograph0')}
strips_sat_x_1_state.calibrated = set()
strips_sat_x_1_state.have_image = set()
strips_sat_x_1_state.power_on = set()

strips_sat_x_1_goals = State('strips_sat_x_1_goals')
strips_sat_x_1_goals.have_image = {('phenomenon12','thermograph0'),('phenomenon13','image1'),('phenomenon18','image1'),('phenomenon5','image1'),('phenomenon7','thermograph0'),('planet15','image2'),('planet17','image2'),('planet21','thermograph0'),('planet23','image1'),('planet8','image2'),('star10','thermograph3'),('star14','thermograph4'),('star19','thermograph4'),('star20','thermograph4'),('star22','thermograph3'),('star9','thermograph0')}
strips_sat_x_1_goals.pointing = {('satellite0','planet21'),('satellite2','star14'),('satellite5','planet17')}

