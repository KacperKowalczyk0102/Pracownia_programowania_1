# Zadanie 10

class TV:
    
    def __init__(self):
        self.is_on = False
        
    def turn_on(self):
        self.is_on = True
        
    def turn_off(self):
        self.is_on = False
        
    def show_status(self):
        if self.is_on == True:
            print("TV is on")
        else:
            print("TV is off")
        
# a        
tv_set = TV()
# b
tv_set.show_status()
# c
tv_set.turn_on()
# d
tv_set.show_status()
# e
tv_set.turn_off()
# f
tv_set.show_status()
