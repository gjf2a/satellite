from pyhop_anytime import *

strips_sat_x_1_state = State('strips_sat_x_1_state')
strips_sat_x_1_state.calibration_target = {('instrument0','star1'):True,('instrument1','star2'):True,('instrument2','star0'):True,('instrument3','star0'):True}
strips_sat_x_1_state.on_board = {('instrument0','satellite0'):True,('instrument1','satellite0'):True,('instrument2','satellite0'):True,('instrument3','satellite1'):True}
strips_sat_x_1_state.pointing = {('satellite0','star4'):True,('satellite1','star0'):True}
strips_sat_x_1_state.power_avail = {'satellite0':True,'satellite1':True}
strips_sat_x_1_state.supports = {('instrument0','infrared0'):True,('instrument0','spectrograph2'):True,('instrument1','image1'):True,('instrument2','image1'):True,('instrument2','infrared0'):True,('instrument3','image1'):True,('instrument3','infrared0'):True,('instrument3','spectrograph2'):True}
strips_sat_x_1_state.calibrated = {}
strips_sat_x_1_state.have_image = {}
strips_sat_x_1_state.power_on = {}

strips_sat_x_1_goals = State('strips_sat_x_1_goals')
strips_sat_x_1_goals.have_image = {('phenomenon5','spectrograph2'):True,('phenomenon7','spectrograph2'):True,('star3','infrared0'):True,('star4','spectrograph2'):True}
strips_sat_x_1_goals.pointing = {('satellite0','phenomenon5'):True}

