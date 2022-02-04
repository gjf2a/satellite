from pyhop_anytime import *

strips_sat_x_1_state = State('strips_sat_x_1_state')
strips_sat_x_1_state.calibration_target = {('instrument0','groundstation3'):True,('instrument1','groundstation3'):True,('instrument2','groundstation3'):True,('instrument3','star1'):True,('instrument4','groundstation3'):True,('instrument5','groundstation3'):True,('instrument6','star4'):True,('instrument7','star0'):True,('instrument8','groundstation3'):True}
strips_sat_x_1_state.on_board = {('instrument0','satellite0'):True,('instrument1','satellite0'):True,('instrument2','satellite1'):True,('instrument3','satellite2'):True,('instrument4','satellite2'):True,('instrument5','satellite3'):True,('instrument6','satellite4'):True,('instrument7','satellite4'):True,('instrument8','satellite4'):True}
strips_sat_x_1_state.pointing = {('satellite0','star19'):True,('satellite1','planet17'):True,('satellite2','planet7'):True,('satellite3','star4'):True,('satellite4','phenomenon5'):True}
strips_sat_x_1_state.power_avail = {'satellite0':True,'satellite1':True,'satellite2':True,'satellite3':True,'satellite4':True}
strips_sat_x_1_state.supports = {('instrument0','image4'):True,('instrument1','image4'):True,('instrument1','thermograph1'):True,('instrument2','image4'):True,('instrument2','thermograph0'):True,('instrument2','thermograph2'):True,('instrument3','image3'):True,('instrument3','image4'):True,('instrument4','image3'):True,('instrument5','image4'):True,('instrument5','thermograph1'):True,('instrument6','image3'):True,('instrument6','thermograph0'):True,('instrument6','thermograph1'):True,('instrument7','thermograph0'):True,('instrument7','thermograph2'):True,('instrument8','image3'):True,('instrument8','thermograph2'):True}
strips_sat_x_1_state.calibrated = {}
strips_sat_x_1_state.have_image = {}
strips_sat_x_1_state.power_on = {}

strips_sat_x_1_goals = State('strips_sat_x_1_goals')
strips_sat_x_1_goals.have_image = {('phenomenon12','image3'):True,('phenomenon18','image3'):True,('phenomenon27','thermograph1'):True,('phenomenon5','thermograph1'):True,('planet10','thermograph1'):True,('planet11','thermograph2'):True,('planet13','thermograph1'):True,('planet15','thermograph0'):True,('planet16','image3'):True,('planet17','image4'):True,('planet23','thermograph1'):True,('planet24','thermograph2'):True,('planet25','thermograph1'):True,('planet28','thermograph2'):True,('planet29','thermograph0'):True,('planet6','image4'):True,('planet7','image3'):True,('planet8','image3'):True,('planet9','thermograph0'):True,('star14','image3'):True,('star19','thermograph0'):True,('star21','thermograph1'):True,('star22','image4'):True,('star26','thermograph0'):True}
strips_sat_x_1_goals.pointing = {('satellite1','phenomenon5'):True,('satellite2','planet11'):True,('satellite4','planet11'):True}

