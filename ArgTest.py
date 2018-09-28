#******************************************************************************************************************
# File: LibTest.py
# Course: 17630 Data Structures and Alorithms for Engineers
# Project: Assignment 3 - The Ball Swapping Game
# Copyright: Copyright (c) 2016 Carnegie Mellon University
# Versions:
#	1.0 September 2016 - Initial version (ajl).
#
# Description: This program demonstrates how to use command line arguments in python.
#
# Parameters: Anything thing you want, Any number of arguments.
#
# Dependencies: sys package
#
# Internal Functions: None
#*****************************************************************************************************************

from sys import *

print ("Number of command line arguments:" + str(len(argv)))
for i in range(0,len(argv)):
	print ("argv["+ str(i) +"] = " + argv[i])
