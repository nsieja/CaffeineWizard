#!/usr/bin/env python3

"""
File:        caffeineWizard.py
Author:      Nicholas Sieja
Date:        9/5/2024
Description: Accepts user input for caffeine consumption, 
assumes or accepts input for function constants, 
calculates bodily response to caffeine. Plots response.
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def cafCalculate(caffeine_amount, drinkTime, projectionTime):
    '''
    Return two lists of floats, cafModel and cafTime, that 
    describe the body response to caffeine intake. The
    two returned lists will be passed to the plotting 
    function to generate a graph(s) for the user

    Parameters:
    caffeine_amount:    (int) amount of caffeine consumed (mg)
    drinkTime:          (int) time to consume caffeine (min)
    projectionTime:     (int) time to project out response (min)

    Returns:
    cafModel: (tuple) contains 1 list of floats 
    corresponding to caffeine levels in GI tract, 
    1 list of floats corresponding to caffeine levels in 
    blood, and 1 list of floats that represent the time 
    (independent variable) for plotting purposes

    Precondition:
    caffeine_amount is int, drinkTime is int, projectionTime is int
    '''

    # Parameters
    k1 = 0.0625         # Example value for k1
    k2 = 0.0104         # Example value for k2
    x0 = caffeine_amount/drinkTime  # Constant value of x(t) for t <= T
    T = drinkTime       # Time when x(t) drops to 0

    # Initial conditions
    init_cond = [0,0] #Initial values q(0) and y(0)

    # Time points for ODE solution (in seconds, 1 point per second for 4 hours)
    t = np.linspace(0, projectionTime*60, projectionTime*3600)

    # Solve the ODE system
    solution = odeint(odes, init_cond, t, args=(k1, k2, x0, T))

    # Extract the results for q(t) and y(t)
    q_solution = solution[:, 0]
    y_solution = solution[:, 1]
    cafModel = (q_solution, y_solution, t)

    return cafModel


def odes(state,t,k1,k2,x0,T):
    """
    Compute the derivatives of q and y for the system of ODEs:
    
        dq/dt = -k1 * q + x(t)
        dy/dt = k1 * q - k2 * y
    
    where x(t) describes the caffeine intake
    
    Parameters:
    state:
        (list/array) contains current values of q and y
        state[0] = q(t), state[1] = y(t)
    t : (float) current time that derivatives are being evaluated
    k1: (float) constant rate coefficient for the first ODE
    k2: (float) constant rate coefficient for the second ODE.
    x0: (float) constant value of x(t) for t <= T
    T : (float) time point at which x(t) is 0 (done consuming)

    Returns:
    [dqdt, dydt]: (list) contains the derivatives [dq/dt, dy/dt] 
    at the current time point t
    """

    q, y = state

    if t <= T:
        x_t = x0    # Amt affeine over time T to consume
    else:
        x_t = 0     # Done consuming caffeine

    # Define system of ODEs
    dqdt = -k1*q + x_t      # GI tract kinetics
    dydt = k1*q - k2*y      # Bloodstream kinetics
    
    return [dqdt, dydt]