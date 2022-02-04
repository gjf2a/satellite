from pyhop_anytime import *

strips_sat_x_1_state = State('strips_sat_x_1_state')
strips_sat_x_1_state.calibration_target = {('instrument0','star1'):True,('instrument1','groundstation3'):True,('instrument10','star0'):True,('instrument2','groundstation3'):True,('instrument3','star4'):True,('instrument4','star2'):True,('instrument5','star0'):True,('instrument6','groundstation3'):True,('instrument7','star4'):True,('instrument8','star4'):True,('instrument9','star2'):True}
strips_sat_x_1_state.on_board = {('instrument0','satellite0'):True,('instrument1','satellite0'):True,('instrument10','satellite4'):True,('instrument2','satellite1'):True,('instrument3','satellite1'):True,('instrument4','satellite2'):True,('instrument5','satellite2'):True,('instrument6','satellite3'):True,('instrument7','satellite3'):True,('instrument8','satellite4'):True,('instrument9','satellite4'):True}
strips_sat_x_1_state.pointing = {('satellite0','star0'):True,('satellite1','star4'):True,('satellite2','star1'):True,('satellite3','groundstation3'):True,('satellite4','planet10'):True}
strips_sat_x_1_state.power_avail = {'satellite0':True,'satellite1':True,'satellite2':True,'satellite3':True,'satellite4':True}
strips_sat_x_1_state.supports = {('instrument0','image4'):True,('instrument1','infrared0'):True,('instrument1','spectrograph1'):True,('instrument10','image2'):True,('instrument10','image4'):True,('instrument2','image2'):True,('instrument2','infrared0'):True,('instrument3','infrared0'):True,('instrument3','infrared3'):True,('instrument4','image4'):True,('instrument4','infrared0'):True,('instrument4','spectrograph1'):True,('instrument5','image2'):True,('instrument5','infrared0'):True,('instrument5','infrared3'):True,('instrument6','infrared0'):True,('instrument6','infrared3'):True,('instrument7','image4'):True,('instrument7','infrared3'):True,('instrument7','spectrograph1'):True,('instrument8','image4'):True,('instrument8','spectrograph1'):True,('instrument9','infrared3'):True}
strips_sat_x_1_state.calibrated = {}
strips_sat_x_1_state.have_image = {}
strips_sat_x_1_state.power_on = {}

strips_sat_x_1_goals = State('strips_sat_x_1_goals')
strips_sat_x_1_goals.have_image = {('phenomenon13','image4'):True,('phenomenon14','spectrograph1'):True,('phenomenon8','image4'):True,('planet10','infrared3'):True,('planet5','image4'):True,('planet9','infrared0'):True,('star12','image4'):True,('star15','spectrograph1'):True,('star16','image2'):True,('star6','infrared3'):True,('star7','image4'):True}
strips_sat_x_1_goals.pointing = {('satellite4','planet9'):True}

