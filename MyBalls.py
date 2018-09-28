# ******************************************************************************************************************
# File: MyBalls.py
# Author: Xincheng Huang
# Course: 17630 Data Structures and Alorithms for Engineers
# Project: Assignment 1 - The Ball Swapping Game
# Copyright: Copyright (c) 2018 Carnegie Mellon University
# Versions:
#	1.0 September 2018 - Initial version (Xincheng Huang).
#
# Description: This program demonstrates how to swap the balls step by step.
#
# Parameters: Number of balls in the game
#
# Dependencies: This program is dependent upon the package BallSwap.Lib. It is assumed that this package folder is
#               in the same folder as this program.
#
# Internal Functions: Yes
# *****************************************************************************************************************

from sys import *  # This is the standard Python system package
import BallSwap.Lib  # This is the BallSwap.Lib package

# Check if the ball number matches the rule

# Check of the argument is
if len(argv) != 2:
    print("\nYou must provide the number of balls on the command line. The correct syntax is:")
    print("\npython MyBalls <number of balls>\n")
    input("\nPress enter to continue...")
    quit()

# Check if the input is a digit
if not argv[1].isdigit():
    print("\nYou must provide the number of balls on the command line. The correct syntax is:")
    print("\npython MyBalls <number of balls>\n")
    input("\nPress enter to continue...")
    quit()

# Check if the input is greater than or equal to 4
if int(argv[1]) < 2:
    print("\nThere must be at least 2 balls for the demonstration... 6 or more makes it interesting...")
    input("\nPress enter to continue...")
    quit()

# Check if the input is an even number
if int(argv[1]) % 2 != 0:
    print("\nPlease enter an even number that is bigger than or equal to 2")
    input("\nPress enter to continue...")
    quit()

num = int(argv[1]) + 1  # Add an extra ball position in the window for the space
BallSwap.Lib.InitGameWindow(num)  # Create the game window

balls = []  # Creates a list that represents the ball color and position
steps = 0  # Creates a global integer counter to count all steps
for i in range(0, int(num / 2)):
    # Here we put the red balls in the list
    balls.append(1)

# Here we put the blank space in the middle which is really a black ball
# that matches the window background.

balls.append(0)

# Here we put the blue balls in the list
for i in range(int(num / 2 + 1), num):
    balls.append(2)

# This draws the balls in the game window as specified in the balls array.
BallSwap.Lib.DisplayBalls(balls)

# This demonstrates how to use the click-to-continue feature and how to rewrite
# the balls to the window
# print("\nNow we can display a continue message and wait for a user (you) to")
# print("click the mouse in the game window. Once you clicked in the window, the")
# print("program will continue. ")
# print("\nTo make it interesting,... lets rearrange the balls...")
# print("\nClick in the window to continue...")
#
BallSwap.Lib.ClickToContinue("Click To Start")


#   swap( BallArray[], integer a, integer b )
#   This function switches two integers specified in the BallArray[] by given indexes.
#	The BallArray is an integer array that expects each element of the array to be 0, 1, or 2:
#   The time complexity of this function is O(1)

def swap(list, a, b):
    list[a], list[b] = list[b], list[a]


#	find_zero(list list[])
#   This function finds the first zero in the given list and return its index.
#   If there's no zero in the index, this function should return -1.
#	Notice that in this program, there should be exact one zero in any given lists.
#   The time complexity of this function is O(n)

def find_zero(list):
    for i in range(len(list)):
        if list[i] == 0:
            return i

    # In this program, the controls should never reach here.
    return -1



#   do_job(list balls[],Integer num)
#   This function perform one "round" defined in the paper
#   balls is a list standing for each ball's position
#   num is the number entered by the user

#   In the following comments, moving forward means moving a ball to its target side
#   Moving backward means moving a ball to its original side
#   That is, for red balls, left is backward, right is forward
#   For blue balls, left is forward, right is backward.

def do_job(list, num):
    # Part 1 (As defined in the paper)
    half = int(num / 2)
    zero_index = find_zero(list)

    # Here we do a prepare step for following loops
    # We move the most-right red ball forward by changing its position to the empty position
    swap(list, zero_index, zero_index - 1)
    BallSwap.Lib.DisplayBalls(balls)

    # Here we get the global variable defined before
    global steps

    steps += 1
    BallSwap.Lib.ClickToContinue("Step " + str(steps))

    # In the following loops we perform two steps each round
    # Move a blue ball forward by jumping over a red ball
    # That is from..1012.. to ..1210..
    # Then we move the red ball forwards
    # That is from..1210.. to ..1201..
    # Repeat these two steps until the red ball reaches end of the list or another red ball
    for i in range(half):
        swap(list, zero_index + i + 1, zero_index + i - 1)
        BallSwap.Lib.DisplayBalls(balls)
        steps += 1
        BallSwap.Lib.ClickToContinue("Step " + str(steps))
        swap(list, zero_index + i + 1, zero_index + i)
        BallSwap.Lib.DisplayBalls(balls)
        steps += 1
        BallSwap.Lib.ClickToContinue("Step " + str(steps))

    # Ending Scenario
    # Check if the game has finished
    # Only the last round passes the check
    if list[0] == 2:
        return True

    # Part 2 (As defined in the paper)
    # Here we simply move every blue ball backwards to prepare for the next round
    swap_cont = int(num / 2 - 2)
    for i in range(int(num / 2)):
        swap(list, zero_index + swap_cont - i, zero_index + swap_cont + 1 - i)
        BallSwap.Lib.DisplayBalls(balls)
        steps += 1
        BallSwap.Lib.ClickToContinue("Step " + str(steps))
    return False

#   Main routine, repeats until the game finishes
while True:
    if do_job(balls, num):
        break

# This redraws the balls in the game window as specified in the balls array.
BallSwap.Lib.DisplayBalls(balls)
# This demonstrates how to end the game and clear the window.
BallSwap.Lib.EndGame("Finished in\n"+str(steps)+" steps")

