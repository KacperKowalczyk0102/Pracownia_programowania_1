# Zadanie 11

class TV:
    
    def __init__(self):
        self.is_on = False
        self.channel_on = 1
        
    def turn_on(self):
        self.is_on = True
        
    def turn_off(self):
        self.is_on = False
        
    def show_status(self):
        if self.is_on == True:
            print(f"TV is on, channel {self.channel_on}")
        else:
            print("TV is off")

tv_set = TV()
tv_set.turn_on()
tv_set.show_status()
        
