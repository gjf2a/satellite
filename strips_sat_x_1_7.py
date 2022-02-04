from pyhop_anytime import *

strips_sat_x_1_state = State('strips_sat_x_1_state')
strips_sat_x_1_state.calibration_target = {('instrument0','star4'):True,('instrument1','star0'):True,('instrument10','star3'):True,('instrument11','star1'):True,('instrument12','star3'):True,('instrument2','star4'):True,('instrument3','star1'):True,('instrument4','star1'):True,('instrument5','star3'):True,('instrument6','star0'):True,('instrument7','star3'):True,('instrument8','star3'):True,('instrument9','star1'):True}
strips_sat_x_1_state.on_board = {('instrument0','satellite0'):True,('instrument1','satellite0'):True,('instrument10','satellite3'):True,('instrument11','satellite3'):True,('instrument12','satellite4'):True,('instrument2','satellite0'):True,('instrument3','satellite1'):True,('instrument4','satellite1'):True,('instrument5','satellite1'):True,('instrument6','satellite1'):True,('instrument7','satellite2'):True,('instrument8','satellite2'):True,('instrument9','satellite2'):True}
strips_sat_x_1_state.pointing = {('satellite0','star8'):True,('satellite1','phenomenon21'):True,('satellite2','star4'):True,('satellite3','phenomenon16'):True,('satellite4','phenomenon18'):True}
strips_sat_x_1_state.power_avail = {'satellite0':True,'satellite1':True,'satellite2':True,'satellite3':True,'satellite4':True}
strips_sat_x_1_state.supports = {('instrument0','thermograph0'):True,('instrument0','thermograph2'):True,('instrument0','thermograph4'):True,('instrument1','thermograph3'):True,('instrument10','thermograph2'):True,('instrument11','thermograph0'):True,('instrument11','thermograph2'):True,('instrument11','thermograph4'):True,('instrument12','thermograph4'):True,('instrument2','image1'):True,('instrument3','thermograph3'):True,('instrument4','image1'):True,('instrument5','thermograph3'):True,('instrument6','image1'):True,('instrument6','thermograph0'):True,('instrument6','thermograph2'):True,('instrument7','thermograph0'):True,('instrument8','thermograph2'):True,('instrument8','thermograph3'):True,('instrument8','thermograph4'):True,('instrument9','thermograph2'):True,('instrument9','thermograph3'):True}
strips_sat_x_1_state.calibrated = {}
strips_sat_x_1_state.have_image = {}
strips_sat_x_1_state.power_on = {}

strips_sat_x_1_goals = State('strips_sat_x_1_goals')
strips_sat_x_1_goals.have_image = {('phenomenon13','thermograph2'):True,('phenomenon17','thermograph4'):True,('phenomenon18','image1'):True,('phenomenon21','image1'):True,('phenomenon5','thermograph4'):True,('planet19','thermograph2'):True,('planet20','thermograph4'):True,('planet7','image1'):True,('star10','image1'):True,('star15','thermograph2'):True,('star22','thermograph3'):True,('star8','thermograph3'):True,('star9','image1'):True}

