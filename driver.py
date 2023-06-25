#!/usr/bin/python
#program name: driver.py
#YOUR name: Jorge Leon Barreno
#date: July 12, 2021
#program description: This program Prompts and gets input from user
#compiler version: 3.9.5
#non-standard libraries: function_lib
#operating system: Windows 10
"""
import our made function library that hold three functions
Choice - that displays user choice for input.
Imageprocessing-
Cluster analysis- 
"""
import function_lib

function_lib.Choice()
option = int(input("Enter which number option you would like to run: "))
while option !=0:
    if option ==1:
        function_lib.makeGrayScale()
        function_lib.makeDoubleImage()
        print() #using for line break
    elif option ==2:
        function_lib.clusterAnalysis("avg_marathon_times_[seconds].csv")
        print() #using for line break
    else:
        print("invalid option.")
        print()#using for line break
    function_lib.Choice()
    option = int(input("Enter which number option you would like to run: " ))
print("Goodbye!")
