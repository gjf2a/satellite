from pyhop_anytime import *

strips_sat_x_1_state = State('strips_sat_x_1_state')
strips_sat_x_1_state.calibration_target = {('instrument0','star3'):True,('instrument1','star4'):True,('instrument10','star2'):True,('instrument2','star2'):True,('instrument3','star2'):True,('instrument4','star3'):True,('instrument5','star3'):True,('instrument6','star2'):True,('instrument7','star0'):True,('instrument8','groundstation1'):True,('instrument9','star0'):True}
strips_sat_x_1_state.on_board = {('instrument0','satellite0'):True,('instrument1','satellite0'):True,('instrument10','satellite4'):True,('instrument2','satellite0'):True,('instrument3','satellite1'):True,('instrument4','satellite1'):True,('instrument5','satellite1'):True,('instrument6','satellite2'):True,('instrument7','satellite3'):True,('instrument8','satellite4'):True,('instrument9','satellite4'):True}
strips_sat_x_1_state.pointing = {('satellite0','star0'):True,('satellite1','planet11'):True,('satellite2','phenomenon6'):True,('satellite3','planet10'):True,('satellite4','star9'):True}
strips_sat_x_1_state.power_avail = {'satellite0':True,'satellite1':True,'satellite2':True,'satellite3':True,'satellite4':True}
strips_sat_x_1_state.supports = {('instrument0','image4'):True,('instrument0','infrared1'):True,('instrument1','image2'):True,('instrument1','image4'):True,('instrument1','spectrograph0'):True,('instrument10','image2'):True,('instrument10','image4'):True,('instrument10','infrared1'):True,('instrument2','image2'):True,('instrument3','image2'):True,('instrument3','image3'):True,('instrument3','image4'):True,('instrument4','image2'):True,('instrument4','image3'):True,('instrument5','image4'):True,('instrument5','infrared1'):True,('instrument5','spectrograph0'):True,('instrument6','image2'):True,('instrument6','spectrograph0'):True,('instrument7','image3'):True,('instrument7','image4'):True,('instrument7','spectrograph0'):True,('instrument8','image3'):True,('instrument8','image4'):True,('instrument8','infrared1'):True,('instrument9','image4'):True}
strips_sat_x_1_state.calibrated = {}
strips_sat_x_1_state.have_image = {}
strips_sat_x_1_state.power_on = {}

strips_sat_x_1_goals = State('strips_sat_x_1_goals')
strips_sat_x_1_goals.have_image = {('phenomenon12','image3'):True,('phenomenon13','spectrograph0'):True,('phenomenon6','image3'):True,('phenomenon7','infrared1'):True,('phenomenon8','image2'):True,('planet10','image4'):True,('planet11','spectrograph0'):True,('planet5','image2'):True,('star14','image4'):True,('star9','image3'):True}
strips_sat_x_1_goals.pointing = {('satellite0','phenomenon7'):True,('satellite3','star9'):True,('satellite4','planet5'):True}

