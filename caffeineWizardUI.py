#!/usr/bin/env python3

"""
File:        caffeineWizardUI.py
Author:      Nicholas Sieja
Date:        9/15/2024
Description: Accepts user input for caffeine consumption, 
assumes or accepts input for function constants, 
calculates bodily response to caffeine. Plots response.
"""

from pyforms import BaseWidget
from pyforms.controls import ControlText, ControlButton
from caffeineWizard import cafCalculate
import matplotlib.pyplot as plt

class CaffeineApp(BaseWidget):
    def __init__(self):
        super().__init__('Caffeine Calculator')
        
        self._caffeine = ControlText('Caffeine (mg)', '60')
        self._drink_time = ControlText('Drink Time (min)', '10')
        self._projection_time = ControlText('Projection Time (hrs)', '4')
        
        self._run_btn = ControlButton('Run Calculation')
        self._run_btn.value = self.__run_calculation
    
    def __run_calculation(self):
        caf = int(self._caffeine.value)
        drink_time = int(self._drink_time.value)
        projection_time = int(self._projection_time.value)
        
        result = cafCalculate(caf, drink_time, projection_time)
        plt.plot(result[2], result[0], label='GI Tract Caffeine Level')
        plt.plot(result[2], result[1], label='Bloodstream Caffeine Level')
        plt.xlabel('Time (min)')
        plt.ylabel('Caffeine (mg)')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    from pyforms import start_app
    start_app(CaffeineApp)
