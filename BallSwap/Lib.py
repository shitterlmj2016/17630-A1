#******************************************************************************************************************
# File:BallSwap.Lib.py
# Course: 17630 Data Structures and Alorithms for Engineers
# Project: Assignment 3 - The Ball Swapping Game
# Copyright: Copyright (c) 2016 Carnegie Mellon University
# Versions:
#	1.0 September 2016 - Initial version of BallGameLib (ajl).
#
# Description: This package provides a number of functions designed to be use to display the balls for the ball
# swapping game. The specific functions are described below.
#
# Parameters: None
#
# Dependencies: John Zelle Graphics Package. This package is free to use and is available at:
# 				mcsp.wartburg.edu/zelle/python/graphics.py
# 				A copy of this library (graphics.py) has been provided in the assignment archive. The file
#				graphics.py should be moved to the Python installation's Lib folder.
#
# Internal Functions:
#		InitGameWindow( integer NumBalls )
#		DisplayBalls( integer BallArray[] )
#		ClickToContinue( string msg )
#		EndGame( string msg )
#*****************************************************************************************************************

from graphics import *

#*****************************************************************************************************************
#	Function:InitGameWindow( integer NumBalls ) - This function sets up the game window. It will automatically
#	determine the necessary width of the window based on the number of balls in the game. The NumBalls variable
#	includes the blue balls, the red balls, plus the empty space. This function does not check to ensure that the
#	number of balls specified falls within the width of the console - this is the responsibility of the caller.
#*****************************************************************************************************************

def InitGameWindow( NumBalls ):

	global __ballcnt__	# This is the number of balls in the game. This is used by DisplayBalls to update the game
						# display.
	global __win__		# This is the game window pointer. This is used by DisplayBalls to update the game display.

	# Here we essentially create the game window.

	__ballcnt__ = NumBalls
	__win__ = GraphWin("The Ball Swap", NumBalls * 25, 50)
	__win__.setBackground('black')

#*****************************************************************************************************************
#	DisplayBalls( integer BallArray[] ) - This function displays the balls specified in the BallArray[]. The
#	BallArray is an integer array that expects each element of the array to be 0, 1, or 2 as follows:
#		A 0 indicates that that a space should be displayed in position i (where i is the array index)
#		A 1 indicates that a red ball should be displayed in position i
#		A 2 indicates that a blue ball should be displayed in position i
#
#	This function will display the specified balls in the game window int the order the appear in the array, 0 to
#	NumBalls-1, from left to right in the game window. This function assumes that the BallArray has the number of
#	balls including	the initial space specified in call to InitGameWindow( integer NumBalls ). If the array as more
#	or less elements than NumBalls the this function will not work properly.def DisplayBalls(BallArray):
#*****************************************************************************************************************

def DisplayBalls(BallArray):

	NumBalls = __ballcnt__
	win = __win__
	pos = 10

	# In the following loop we traverse the entire array and print each ball in the game window, left to right
	# filling it with the color specified by the number specified in the BallArray
	for i in range(NumBalls):
		if BallArray[i] == 0: 		#	Blank space
			tempball = Circle(Point(pos, 12), 10)
			tempball.draw(win)
			tempball.setFill("black");
		elif BallArray[i] == 1:		#	Red Ball
			tempball = Circle(Point(pos, 12), 10)
			tempball.draw(win)
			tempball.setFill("red");
		elif BallArray[i] == 2:		#	Blue Ball
			tempball = Circle(Point(pos, 12), 10)
			tempball.draw(win)
			tempball.setFill("blue");

		pos = pos + 25				# 	Increment to the next position in the window

#*****************************************************************************************************************
#	ClickToContinue( string msg ) - This function will display the string specified in msg in the game window.
#	After displaying the message, the function will wait until the user clicks anywhere in the game window.
#	Once they click in the game window, the program will resume execution.
#*****************************************************************************************************************

def ClickToContinue(msg):
	message = Text(Point(__win__.getWidth()/2, 35), msg)	# Create the text
	message.setTextColor('yellow')							# Set text color to yellow
	message.draw(__win__)									# Display the message
	__win__.getMouse()										# Wait for a mouse click in the game window
	message = Text(Point(__win__.getWidth()/2, 35), msg)	# Clear the text and continue execution
	message.setTextColor('black')
	message.draw(__win__)


#*****************************************************************************************************************
#	EndGame( string msg ) - This function will display the string specified in msg in the game window.
#	After displaying the message, the function will wait until the user clicks anywhere in the game window.
#	Once they click in the game window, the program will terminate the game window and continue exectution.
#*****************************************************************************************************************

def EndGame(msg):
	message = Text(Point(__win__.getWidth()/2, 35), msg)	# Create the text
	message.setTextColor('yellow')							# Set text color to yellow
	message.draw(__win__)									# Display the message
	__win__.getMouse()										# Wait for a mouse click in the game window
	__win__.close()											# Close the gamewindow
