#******************************************************************************************************************
# File: LibTest.py
# Course: 17630 Data Structures and Alorithms for Engineers
# Project: Assignment 3 - The Ball Swapping Game
# Copyright: Copyright (c) 2016 Carnegie Mellon University
# Versions:
#	1.0 September 2016 - Initial version (ajl).
#
# Description: This program demonstrates how to use the BallSwap.Lib works.
#
# Parameters: Number of balls in the game
#
# Dependencies: This program is dependent upon the package BallSwap.Lib. It is assumed that this package folder is
#               in the same folder as this program.
#
# Internal Functions: None
#*****************************************************************************************************************

from sys import *           # This is the standard Python system package
import BallSwap.Lib         # This is the BallSwap.Lib package

if len(argv) < 2:
        print("\nYou must provide the number of balls on the command line. The correct syntax is:")
        print("\npython LibTest <number of balls>\n")
        input("\nPress enter to continue...")
        quit()

if int(argv[1]) < 4:
        print("\nThere must be at least 4 balls for the demonstration... 6 or more makes it interesting...")
        input("\nPress enter to continue...")
        quit()

print("\nThis demo is designed to illustrate how to use the BallSwap.Lib library. While your application must")
print("not have any user interaction through the command line, this program will demonstrate the use of the")
print("BallSwap.Lib library through command line interactions. This is to explain what is happening at each")
print("step of the process so you can follow along reading the source code.")

print("\nOK. Lets create the Game Window for " + argv[1] + " balls.")
input("\nPress enter to continue...")

num = int(argv[1]) + 1                    # Add an extra ball position in the window for the space
BallSwap.Lib.InitGameWindow(num)    # Create the game window

print("\nOK. Now we put some balls in the window. Half will be red...")
print("Half will be blue... in the middle there will be a space.")
input("\nPress enter to continue...")

balls = []  # Creates a list that represents the ball color and position

for i in range(0, int(num/2)):
    # Here we put the red balls in the list
    balls.append(1)

# Here we put the blank space in the middle which is really a black ball
# that matches the window background.

balls.append(0)

# Here we put the blue balls in the list
for i in range(int(num/2+1), num):
    balls.append(2)

# This draws the balls in the game window as specified in the balls array.
BallSwap.Lib.DisplayBalls(balls)

# This demonstrates how to use the click-to-continue feature and how to rewrite
# the balls to the window
print("\nNow we can display a continue message and wait for a user (you) to")
print("click the mouse in the game window. Once you clicked in the window, the")
print("program will continue. ")
print("\nTo make it interesting,... lets rearrange the balls...")
print("\nClick in the window to continue...")

BallSwap.Lib.ClickToContinue("Click Here")

# Here we rearrange the contents of the Ball swap array. Note that I can directly
# reference the array elements since they were created above - so no need to append()
# these values. What this does is put alternating red, blue balls and still leaves the
# space in the middle.

toggle = 0;

for i in range(0, num):
    if i == int(num/2):
        balls[i] = 0
    elif toggle == 0:
        balls[i] = 1
        toggle = 1
    else:
        balls[i] = 2
        toggle = 0

# This redraws the balls in the game window as specified in the balls array.
BallSwap.Lib.DisplayBalls(balls)

# This demonstrates how to end the game and clear the window.
print("\nOoooh... pretty eh? You can redraw the balls in the window simply by")
print("changing the numbers in the balls[] array...")
print("\nNow we can display a final message and wait for a user (you) to")
print("click the mouse in the game window. Once you clicked in the window, the")
print("window will be destroyed. ")
print("\nClick in the window to continue...")

BallSwap.Lib.EndGame("Thats All")

print("\nThat ends the demo... I hope this helps...")
