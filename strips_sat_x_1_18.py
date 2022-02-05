from pyhop_anytime import *

strips_sat_x_1_state = State('strips_sat_x_1_state')
strips_sat_x_1_state.calibration_target = {('instrument0','groundstation3'),('instrument1','groundstation3'),('instrument2','groundstation3'),('instrument3','star1'),('instrument4','groundstation3'),('instrument5','groundstation3'),('instrument6','star4'),('instrument7','star0'),('instrument8','groundstation3')}
strips_sat_x_1_state.on_board = {('instrument0','satellite0'),('instrument1','satellite0'),('instrument2','satellite1'),('instrument3','satellite2'),('instrument4','satellite2'),('instrument5','satellite3'),('instrument6','satellite4'),('instrument7','satellite4'),('instrument8','satellite4')}
strips_sat_x_1_state.pointing = {('satellite0','star19'),('satellite1','planet17'),('satellite2','planet7'),('satellite3','star4'),('satellite4','phenomenon5')}
strips_sat_x_1_state.power_avail = {'satellite0','satellite1','satellite2','satellite3','satellite4'}
strips_sat_x_1_state.supports = {('instrument0','image4'),('instrument1','image4'),('instrument1','thermograph1'),('instrument2','image4'),('instrument2','thermograph0'),('instrument2','thermograph2'),('instrument3','image3'),('instrument3','image4'),('instrument4','image3'),('instrument5','image4'),('instrument5','thermograph1'),('instrument6','image3'),('instrument6','thermograph0'),('instrument6','thermograph1'),('instrument7','thermograph0'),('instrument7','thermograph2'),('instrument8','image3'),('instrument8','thermograph2')}
strips_sat_x_1_state.calibrated = set()
strips_sat_x_1_state.have_image = set()
strips_sat_x_1_state.power_on = set()

strips_sat_x_1_goals = State('strips_sat_x_1_goals')
strips_sat_x_1_goals.have_image = {('phenomenon12','image3'),('phenomenon18','image3'),('phenomenon27','thermograph1'),('phenomenon5','thermograph1'),('planet10','thermograph1'),('planet11','thermograph2'),('planet13','thermograph1'),('planet15','thermograph0'),('planet16','image3'),('planet17','image4'),('planet23','thermograph1'),('planet24','thermograph2'),('planet25','thermograph1'),('planet28','thermograph2'),('planet29','thermograph0'),('planet6','image4'),('planet7','image3'),('planet8','image3'),('planet9','thermograph0'),('star14','image3'),('star19','thermograph0'),('star21','thermograph1'),('star22','image4'),('star26','thermograph0')}
strips_sat_x_1_goals.pointing = {('satellite1','phenomenon5'),('satellite2','planet11'),('satellite4','planet11')}

