'''
Created by Roman Beya
Created on 27-oct-2017
Created for ICS3U
This program calculates a grade point average with input by the user
'''
import ui

# GLOBAL variables
counter = 0
sum_of_total_marks = 0

def record_marks_touch_up_inside(sender):
	# Each time this button is pressed, a counter variable will increment by 1
	global counter
	counter = counter + 1
	# This procedure will also record the sum of all marks inputted by the user
	global sum_of_total_marks
	sum_of_total_marks = sum_of_total_marks + int(view['enter_marks_textfield'].text) 
	
def calculate_grade_point_average_touch_up_inside(sender):
	# This procedure will calculate the average using the sum of inputted numbers / counter
	global counter
	global sum_of_total_marks
	# Average = Sigma(marks) divided the quantity that the counter has incremented by
	grade_point_average = sum_of_total_marks / counter
	view['grade_point_average_label'].text = "Your grade point average is: {}%".format(grade_point_average)
	
view = ui.load_view()
view.present('sheet')
