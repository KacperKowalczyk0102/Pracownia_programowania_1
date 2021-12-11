# Zadnie 17

import random

class Thermometer:

    def __init__(self):
        self.is_on= False
        self.temperature = 0

    def turn_on(self):
        if self.is_on == False:
            self.is_on = True
        else:
            print("Thermometer is already ON!")


    def turn_off(self):
        if self.is_on == True:
            self.is_on = False
        else:
            print("Thermometer is already OFF!")


    def measure(self):
        if self.is_on == True:
            self.temperature = round(random.uniform(34.0, 42.0), 1)
            print("Temperature measured :)")
        else:
            print("Thermometer id OFF!")


    def display(self):
        if self.is_on == True:
            if self.temperature == 0:
                print(f"First, take a measurement!")
            else:
                print(f"Temperature: {self.temperature}")
        else:
            print("Thermometer is OFF!")


th1 = Thermometer()
th1.turn_on()
th1.display()
th1.measure()
th1.display()
th1.turn_off()
th1.turn_off()




