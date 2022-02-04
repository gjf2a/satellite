from pyhop_anytime import *

strips_sat_x_1_state = State('strips_sat_x_1_state')
strips_sat_x_1_state.calibration_target = {('instrument0','star3'):True,('instrument1','star2'):True,('instrument2','star4'):True,('instrument3','groundstation1'):True,('instrument4','star4'):True,('instrument5','star0'):True,('instrument6','star3'):True,('instrument7','star0'):True,('instrument8','star3'):True,('instrument9','star4'):True}
strips_sat_x_1_state.on_board = {('instrument0','satellite0'):True,('instrument1','satellite0'):True,('instrument2','satellite0'):True,('instrument3','satellite1'):True,('instrument4','satellite1'):True,('instrument5','satellite1'):True,('instrument6','satellite2'):True,('instrument7','satellite2'):True,('instrument8','satellite3'):True,('instrument9','satellite3'):True}
strips_sat_x_1_state.pointing = {('satellite0','phenomenon14'):True,('satellite1','star4'):True,('satellite2','star6'):True,('satellite3','phenomenon5'):True}
strips_sat_x_1_state.power_avail = {'satellite0':True,'satellite1':True,'satellite2':True,'satellite3':True}
strips_sat_x_1_state.supports = {('instrument0','image0'):True,('instrument0','thermograph1'):True,('instrument1','spectrograph3'):True,('instrument1','thermograph1'):True,('instrument1','thermograph2'):True,('instrument2','spectrograph3'):True,('instrument3','image0'):True,('instrument3','thermograph2'):True,('instrument4','thermograph1'):True,('instrument5','spectrograph3'):True,('instrument5','thermograph1'):True,('instrument5','thermograph2'):True,('instrument6','thermograph1'):True,('instrument6','thermograph2'):True,('instrument7','image0'):True,('instrument7','thermograph1'):True,('instrument7','thermograph2'):True,('instrument8','image0'):True,('instrument9','image0'):True,('instrument9','spectrograph3'):True,('instrument9','thermograph1'):True}
strips_sat_x_1_state.calibrated = {}
strips_sat_x_1_state.have_image = {}
strips_sat_x_1_state.power_on = {}

strips_sat_x_1_goals = State('strips_sat_x_1_goals')
strips_sat_x_1_goals.have_image = {('phenomenon12','image0'):True,('phenomenon13','thermograph1'):True,('phenomenon14','thermograph2'):True,('phenomenon5','thermograph1'):True,('phenomenon8','image0'):True,('phenomenon9','image0'):True,('planet11','thermograph2'):True,('star10','spectrograph3'):True,('star6','thermograph1'):True,('star7','spectrograph3'):True}

