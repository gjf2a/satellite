from pyhop_anytime import *

strips_sat_x_1_state = State('strips_sat_x_1_state')
strips_sat_x_1_state.calibration_target = {('instrument0','star0'):True,('instrument1','star2'):True,('instrument2','star3'):True,('instrument3','star4'):True,('instrument4','star4'):True,('instrument5','groundstation1'):True,('instrument6','star4'):True,('instrument7','star2'):True,('instrument8','star2'):True,('instrument9','star4'):True}
strips_sat_x_1_state.on_board = {('instrument0','satellite0'):True,('instrument1','satellite0'):True,('instrument2','satellite0'):True,('instrument3','satellite1'):True,('instrument4','satellite1'):True,('instrument5','satellite2'):True,('instrument6','satellite3'):True,('instrument7','satellite4'):True,('instrument8','satellite4'):True,('instrument9','satellite4'):True}
strips_sat_x_1_state.pointing = {('satellite0','planet16'):True,('satellite1','star4'):True,('satellite2','star15'):True,('satellite3','phenomenon6'):True,('satellite4','star14'):True}
strips_sat_x_1_state.power_avail = {'satellite0':True,'satellite1':True,'satellite2':True,'satellite3':True,'satellite4':True}
strips_sat_x_1_state.supports = {('instrument0','infrared1'):True,('instrument0','spectrograph4'):True,('instrument1','infrared0'):True,('instrument1','infrared1'):True,('instrument2','infrared0'):True,('instrument2','infrared1'):True,('instrument3','infrared0'):True,('instrument3','spectrograph4'):True,('instrument4','infrared0'):True,('instrument4','infrared3'):True,('instrument4','thermograph2'):True,('instrument5','infrared1'):True,('instrument6','infrared1'):True,('instrument7','infrared1'):True,('instrument7','infrared3'):True,('instrument8','infrared0'):True,('instrument8','infrared3'):True,('instrument8','spectrograph4'):True,('instrument9','infrared1'):True,('instrument9','infrared3'):True,('instrument9','spectrograph4'):True}
strips_sat_x_1_state.calibrated = {}
strips_sat_x_1_state.have_image = {}
strips_sat_x_1_state.power_on = {}

strips_sat_x_1_goals = State('strips_sat_x_1_goals')
strips_sat_x_1_goals.have_image = {('phenomenon13','spectrograph4'):True,('phenomenon17','spectrograph4'):True,('phenomenon21','thermograph2'):True,('phenomenon24','infrared0'):True,('phenomenon6','spectrograph4'):True,('planet10','thermograph2'):True,('planet11','infrared3'):True,('planet16','infrared1'):True,('planet20','thermograph2'):True,('planet5','infrared0'):True,('planet8','infrared1'):True,('star14','thermograph2'):True,('star15','infrared3'):True,('star18','spectrograph4'):True,('star19','thermograph2'):True,('star22','infrared1'):True,('star23','spectrograph4'):True,('star7','infrared0'):True,('star9','spectrograph4'):True}

