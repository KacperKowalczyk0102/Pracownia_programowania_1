# Zadanie 12

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
            
    def new_channel(self, new_channel_on):
        self.channel_on = new_channel_on


# a
tv_set = TV()
# b
tv_set.show_status()
# c
tv_set.turn_on()
# d
tv_set.show_status()
# e
tv_set.new_channel(5)
# f
tv_set.show_status()
# g
tv_set.turn_off()
# h
tv_set.show_status()

        

