from pyhop_anytime import *

strips_sat_x_1_state = State('strips_sat_x_1_state')
strips_sat_x_1_state.calibration_target = {('instrument0','star0'):True,('instrument1','star2'):True,('instrument2','star2'):True}
strips_sat_x_1_state.on_board = {('instrument0','satellite0'):True,('instrument1','satellite1'):True,('instrument2','satellite1'):True}
strips_sat_x_1_state.pointing = {('satellite0','star6'):True,('satellite1','star0'):True}
strips_sat_x_1_state.power_avail = {'satellite0':True,'satellite1':True}
strips_sat_x_1_state.supports = {('instrument0','infrared0'):True,('instrument0','thermograph2'):True,('instrument1','infrared0'):True,('instrument1','infrared1'):True,('instrument1','thermograph2'):True,('instrument2','infrared1'):True,('instrument2','thermograph2'):True}
strips_sat_x_1_state.calibrated = {}
strips_sat_x_1_state.have_image = {}
strips_sat_x_1_state.power_on = {}

strips_sat_x_1_goals = State('strips_sat_x_1_goals')
strips_sat_x_1_goals.have_image = {('phenomenon8','thermograph2'):True,('phenomenon9','infrared0'):True,('planet3','infrared1'):True,('planet5','thermograph2'):True,('star4','infrared1'):True,('star6','infrared1'):True,('star7','infrared0'):True}
strips_sat_x_1_goals.pointing = {('satellite1','planet5'):True}

