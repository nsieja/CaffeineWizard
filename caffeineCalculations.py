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
from scipy.integrate import odeint

def cafCalculate(caffeine, drinkTime, projectionTime):
    '''
    Return two lists of floats, cafModel and cafTime, that 
    describe the body response to caffeine intake. The
    two returned lists will be passed to the plotting 
    function to generate a graph(s) for the user

    Parameters:
    caffeine      : (int) amount of caffeine consumed (mg)
    drinkTime     : (int) time to consume caffeine (min)
    projectionTime: (int) time to project out response (min)

    Returns:
    cafModel: (tuple) contains 1 list of floats 
    corresponding to caffeine levels in GI tract, 
    1 list of floats corresponding to caffeine levels in 
    blood, and 1 list of floats that represent the time 
    (independent variable) for plotting purposes

    Precondition:
    caffeine is int, drinkTime is int, projectionTime is int
    '''
    pass

def odes(q,y,t,k1,k2,x0,T):
    """
    Compute the derivatives of q and y for the system of ODEs:
    
        dq/dt = -k1 * q + x(t)
        dy/dt = k1 * q - k2 * y
    
    where x(t) describes the caffeine intake
    
    Parameters:
    q : (float) current value of q(t)
    y : (float) current value of y(t)
    t : (float) current time that derivatives are being evaluated
    k1: (float) constant rate coefficient for the first ODE
    k2: (float) constant rate coefficient for the second ODE.
    x0: (float) constant value of x(t) for t <= T
    T : (float) time point at which x(t) is 0 (done consuming)

    Returns:
    [dqdt, dydt]: (list) contains the derivatives [dq/dt, dy/dt] 
    at the current time point t
    """
    if t <= T:
        x_t = x0    # Amt affeine over time T to consume
    else:
        x_t = 0     # Done consuming caffeine

    # Define system of ODEs
    dqdt = -k1*q + x_t      # GI tract kinetics
    dydt = k1*q - k2*y      # Bloodstream kinetics
    
    return [dqdt, dydt]