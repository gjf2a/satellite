from pyhop_anytime import *

strips_sat_x_1_state = State('strips_sat_x_1_state')
strips_sat_x_1_state.calibration_target = {('instrument0','star1'):True,('instrument1','groundstation0'):True,('instrument2','groundstation2'):True,('instrument3','groundstation4'):True,('instrument4','star1'):True,('instrument5','star1'):True,('instrument6','groundstation4'):True,('instrument7','groundstation0'):True}
strips_sat_x_1_state.on_board = {('instrument0','satellite0'):True,('instrument1','satellite0'):True,('instrument2','satellite0'):True,('instrument3','satellite1'):True,('instrument4','satellite2'):True,('instrument5','satellite2'):True,('instrument6','satellite3'):True,('instrument7','satellite3'):True}
strips_sat_x_1_state.pointing = {('satellite0','star6'):True,('satellite1','groundstation0'):True,('satellite2','star6'):True,('satellite3','groundstation2'):True}
strips_sat_x_1_state.power_avail = {'satellite0':True,'satellite1':True,'satellite2':True,'satellite3':True}
strips_sat_x_1_state.supports = {('instrument0','image1'):True,('instrument0','image3'):True,('instrument1','image3'):True,('instrument2','image0'):True,('instrument3','image0'):True,('instrument3','image2'):True,('instrument4','image0'):True,('instrument4','image1'):True,('instrument5','image0'):True,('instrument5','image1'):True,('instrument5','image2'):True,('instrument6','image0'):True,('instrument6','image1'):True,('instrument6','image2'):True,('instrument7','image0'):True,('instrument7','image1'):True,('instrument7','image3'):True}
strips_sat_x_1_state.calibrated = {}
strips_sat_x_1_state.have_image = {}
strips_sat_x_1_state.power_on = {}

strips_sat_x_1_goals = State('strips_sat_x_1_goals')
strips_sat_x_1_goals.have_image = {('phenomenon5','image0'):True,('planet10','image0'):True,('planet11','image2'):True,('planet8','image0'):True,('planet9','image3'):True,('star6','image1'):True,('star7','image0'):True}
strips_sat_x_1_goals.pointing = {('satellite1','star1'):True,('satellite2','phenomenon5'):True}

