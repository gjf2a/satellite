from pyhop_anytime import *

strips_sat_x_1_state = State('strips_sat_x_1_state')
strips_sat_x_1_state.calibration_target = {('instrument0','groundstation2'):True,('instrument1','groundstation0'):True,('instrument10','groundstation0'):True,('instrument11','groundstation1'):True,('instrument2','groundstation2'):True,('instrument3','groundstation2'):True,('instrument4','groundstation1'):True,('instrument5','groundstation4'):True,('instrument6','groundstation0'):True,('instrument7','groundstation4'):True,('instrument8','groundstation2'):True,('instrument9','groundstation2'):True}
strips_sat_x_1_state.on_board = {('instrument0','satellite0'):True,('instrument1','satellite0'):True,('instrument10','satellite4'):True,('instrument11','satellite5'):True,('instrument2','satellite0'):True,('instrument3','satellite1'):True,('instrument4','satellite2'):True,('instrument5','satellite2'):True,('instrument6','satellite2'):True,('instrument7','satellite3'):True,('instrument8','satellite3'):True,('instrument9','satellite4'):True}
strips_sat_x_1_state.pointing = {('satellite0','phenomenon12'):True,('satellite1','groundstation1'):True,('satellite2','groundstation2'):True,('satellite3','groundstation4'):True,('satellite4','planet15'):True,('satellite5','phenomenon11'):True}
strips_sat_x_1_state.power_avail = {'satellite0':True,'satellite1':True,'satellite2':True,'satellite3':True,'satellite4':True,'satellite5':True}
strips_sat_x_1_state.supports = {('instrument0','image1'):True,('instrument0','thermograph0'):True,('instrument1','image2'):True,('instrument1','thermograph3'):True,('instrument10','image1'):True,('instrument10','thermograph3'):True,('instrument11','image2'):True,('instrument11','thermograph0'):True,('instrument2','image1'):True,('instrument2','thermograph3'):True,('instrument2','thermograph4'):True,('instrument3','image2'):True,('instrument3','thermograph0'):True,('instrument3','thermograph4'):True,('instrument4','image1'):True,('instrument4','thermograph0'):True,('instrument4','thermograph4'):True,('instrument5','thermograph4'):True,('instrument6','image1'):True,('instrument6','thermograph3'):True,('instrument7','image2'):True,('instrument7','thermograph3'):True,('instrument8','thermograph0'):True,('instrument8','thermograph4'):True,('instrument9','image1'):True,('instrument9','image2'):True,('instrument9','thermograph0'):True}
strips_sat_x_1_state.calibrated = {}
strips_sat_x_1_state.have_image = {}
strips_sat_x_1_state.power_on = {}

strips_sat_x_1_goals = State('strips_sat_x_1_goals')
strips_sat_x_1_goals.have_image = {('phenomenon12','thermograph0'):True,('phenomenon13','image1'):True,('phenomenon18','image1'):True,('phenomenon5','image1'):True,('phenomenon7','thermograph0'):True,('planet15','image2'):True,('planet17','image2'):True,('planet21','thermograph0'):True,('planet23','image1'):True,('planet8','image2'):True,('star10','thermograph3'):True,('star14','thermograph4'):True,('star19','thermograph4'):True,('star20','thermograph4'):True,('star22','thermograph3'):True,('star9','thermograph0'):True}
strips_sat_x_1_goals.pointing = {('satellite0','planet21'):True,('satellite2','star14'):True,('satellite5','planet17'):True}

