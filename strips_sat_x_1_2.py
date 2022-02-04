from pyhop_anytime import *

strips_sat_x_1_state = State('strips_sat_x_1_state')
strips_sat_x_1_state.calibration_target = {('instrument0','groundstation2'):True,('instrument1','groundstation1'):True,('instrument2','groundstation0'):True,('instrument3','groundstation0'):True,('instrument4','groundstation2'):True,('instrument5','groundstation1'):True,('instrument6','groundstation1'):True,('instrument7','groundstation1'):True,('instrument8','groundstation0'):True}
strips_sat_x_1_state.on_board = {('instrument0','satellite0'):True,('instrument1','satellite0'):True,('instrument2','satellite0'):True,('instrument3','satellite1'):True,('instrument4','satellite1'):True,('instrument5','satellite1'):True,('instrument6','satellite2'):True,('instrument7','satellite2'):True,('instrument8','satellite2'):True}
strips_sat_x_1_state.pointing = {('satellite0','phenomenon8'):True,('satellite1','groundstation2'):True,('satellite2','phenomenon5'):True}
strips_sat_x_1_state.power_avail = {'satellite0':True,'satellite1':True,'satellite2':True}
strips_sat_x_1_state.supports = {('instrument0','image2'):True,('instrument0','spectrograph1'):True,('instrument0','thermograph0'):True,('instrument1','image2'):True,('instrument1','spectrograph1'):True,('instrument1','thermograph0'):True,('instrument2','image2'):True,('instrument3','spectrograph1'):True,('instrument3','thermograph0'):True,('instrument4','image2'):True,('instrument4','spectrograph1'):True,('instrument5','image2'):True,('instrument5','spectrograph1'):True,('instrument5','thermograph0'):True,('instrument6','image2'):True,('instrument7','image2'):True,('instrument7','thermograph0'):True,('instrument8','image2'):True,('instrument8','spectrograph1'):True,('instrument8','thermograph0'):True}
strips_sat_x_1_state.calibrated = {}
strips_sat_x_1_state.have_image = {}
strips_sat_x_1_state.power_on = {}

strips_sat_x_1_goals = State('strips_sat_x_1_goals')
strips_sat_x_1_goals.have_image = {('phenomenon5','image2'):True,('phenomenon6','image2'):True,('phenomenon8','image2'):True,('planet9','spectrograph1'):True,('star3','thermograph0'):True,('star7','thermograph0'):True}
strips_sat_x_1_goals.pointing = {('satellite0','phenomenon5'):True,('satellite1','groundstation2'):True}

