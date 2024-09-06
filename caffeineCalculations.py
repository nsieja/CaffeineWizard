#!/usr/bin/env

"""
File:        caffeineCalculations.py
Author:      Nicholas Sieja
Date:        9/5/2024
Description: Accepts user input for caffeine consumption, 
assumes or accepts input for function constants, 
calculates bodily response to caffeine.
"""

import numpy as np

def cafCalculate(caffeine, drinkTime, projectionTime):
    '''
    Return two lists of floats, cafModel and cafTime, that 
    describe the body response to caffeine intake. The
    two returned lists will be passed to the plotting 
    function to generate a graph(s) for the user

            Parameters:
                    caffeine (int): The amount of caffeine 
                    consumed in mg

                    drinkTime (int): The amount of time 
                    taken to consume the caffeine in minutes

                    projectionTime (int): The amount of time 
                    over which to calculate and project the 
                    response in minutes

            Returns:
                    cafModel (tuple): tuple containing 1 
                    list of floats corresponding to 
                    caffeine levels in GI tract, 1 list of 
                    floats corresponding to caffeine levels 
                    in blood, and 1 list of floats that 
                    represent the time (independent variable) 
                    for plotting purposes

            Precondition:
                    caffeine is type int, drinkTime is type 
                    int, projectionTime is type int
    '''
    pass