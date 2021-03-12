# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 16:15:50 2021

@author: rayde

In the command prompt or terminal of your choice, change the directory to the path
containing the calculations.py file and then type in "python calculations.py"
You will be prompted to input numbers for calculation. Type the numbers and press enter. 
The calculations will run.

"""

from numpy import std 
from statistics import median
import concurrent.futures

def running_mean(nums, precision):
    return round(sum(nums)/len(nums), precision)

def running_std(nums, precision):
    return round(std(nums), precision)

def running_median(nums, precision):
    return round(median(nums), precision)


if __name__ == "__main__":
    numbers = []

    for line in input("Please enter a list of numbers: ").split():
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
            try:
                numbers.append(float(line.strip('\n')))
                executor.submit(print, running_mean(numbers, precision=3), running_std(numbers, precision=3), 
                                running_median(numbers, precision=3))
            except:
                print("MalformedInputException")