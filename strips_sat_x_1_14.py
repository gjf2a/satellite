from pyhop_anytime import *

strips_sat_x_1_state = State('strips_sat_x_1_state')
strips_sat_x_1_state.calibration_target = {('instrument0','star1'):True,('instrument1','star2'):True,('instrument2','star2'):True,('instrument3','star2'):True,('instrument4','star0'):True}
strips_sat_x_1_state.on_board = {('instrument0','satellite0'):True,('instrument1','satellite1'):True,('instrument2','satellite1'):True,('instrument3','satellite1'):True,('instrument4','satellite2'):True}
strips_sat_x_1_state.pointing = {('satellite0','phenomenon8'):True,('satellite1','star6'):True,('satellite2','star6'):True}
strips_sat_x_1_state.power_avail = {'satellite0':True,'satellite1':True,'satellite2':True}
strips_sat_x_1_state.supports = {('instrument0','infrared1'):True,('instrument0','spectrograph0'):True,('instrument1','infrared3'):True,('instrument2','infrared1'):True,('instrument2','infrared3'):True,('instrument2','thermograph2'):True,('instrument3','infrared1'):True,('instrument3','infrared3'):True,('instrument3','spectrograph0'):True,('instrument4','infrared3'):True}
strips_sat_x_1_state.calibrated = {}
strips_sat_x_1_state.have_image = {}
strips_sat_x_1_state.power_on = {}

strips_sat_x_1_goals = State('strips_sat_x_1_goals')
strips_sat_x_1_goals.have_image = {('phenomenon8','spectrograph0'):True,('planet4','thermograph2'):True,('planet5','spectrograph0'):True,('star10','infrared3'):True,('star6','thermograph2'):True,('star7','infrared3'):True,('star9','infrared1'):True}

