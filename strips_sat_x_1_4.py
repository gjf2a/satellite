from pyhop_anytime import *

strips_sat_x_1_state = State('strips_sat_x_1_state')
strips_sat_x_1_state.calibration_target = {('instrument0','star0'):True,('instrument1','groundstation3'):True,('instrument2','star2'):True,('instrument3','star0'):True,('instrument4','star2'):True,('instrument5','star0'):True,('instrument6','groundstation3'):True,('instrument7','star2'):True,('instrument8','star2'):True}
strips_sat_x_1_state.on_board = {('instrument0','satellite0'):True,('instrument1','satellite1'):True,('instrument2','satellite1'):True,('instrument3','satellite1'):True,('instrument4','satellite2'):True,('instrument5','satellite2'):True,('instrument6','satellite2'):True,('instrument7','satellite3'):True,('instrument8','satellite4'):True}
strips_sat_x_1_state.pointing = {('satellite0','star8'):True,('satellite1','groundstation3'):True,('satellite2','star4'):True,('satellite3','phenomenon9'):True,('satellite4','phenomenon9'):True}
strips_sat_x_1_state.power_avail = {'satellite0':True,'satellite1':True,'satellite2':True,'satellite3':True,'satellite4':True}
strips_sat_x_1_state.supports = {('instrument0','spectrograph4'):True,('instrument1','infrared0'):True,('instrument1','infrared1'):True,('instrument2','infrared0'):True,('instrument2','infrared1'):True,('instrument3','infrared1'):True,('instrument3','spectrograph4'):True,('instrument3','thermograph2'):True,('instrument4','image3'):True,('instrument4','infrared0'):True,('instrument4','infrared1'):True,('instrument5','spectrograph4'):True,('instrument5','thermograph2'):True,('instrument6','infrared0'):True,('instrument7','image3'):True,('instrument8','infrared0'):True,('instrument8','infrared1'):True,('instrument8','spectrograph4'):True}
strips_sat_x_1_state.calibrated = {}
strips_sat_x_1_state.have_image = {}
strips_sat_x_1_state.power_on = {}

strips_sat_x_1_goals = State('strips_sat_x_1_goals')
strips_sat_x_1_goals.have_image = {('phenomenon15','infrared0'):True,('phenomenon7','infrared1'):True,('planet13','spectrograph4'):True,('planet14','thermograph2'):True,('planet16','image3'):True,('planet6','infrared1'):True,('star10','thermograph2'):True,('star11','infrared1'):True,('star17','infrared0'):True,('star5','image3'):True,('star8','image3'):True}
strips_sat_x_1_goals.pointing = {('satellite0','phenomenon9'):True,('satellite1','star4'):True,('satellite4','star11'):True}

