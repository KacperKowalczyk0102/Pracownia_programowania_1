# Zadanie 14

class TV:
    
    def __init__(self):
        self.is_on = False
        self.channel_on = 1
        self.channels_list = []
        
    def turn_on(self):
        self.is_on = True
        
    def turn_off(self):
        self.is_on = False
        
    def show_status(self):
        if self.is_on == True:
            if len(self.channels_list[self.channel_on-1])>0:
                print(f"TV is on, channel {self.channel_on} ({self.channels_list[self.channel_on-1]})")
            else:
                print(f"TV is on, channel {self.channel_on}")
        else:
            print("TV is off")
            
    def new_channel(self, new_channel_on):
        self.channel_on = new_channel_on
    
    def set_channels(self, channels_list):
        self.channels_list = channels_list
        
    def show_channels(self):
        print("Channels list: ")
        if len(self.channels_list)>0:
            for k, n in enumerate(self.channels_list):
                print(f"\t{k+1}. {n}")
        else:
            print("\tEmpty")
      
      
tv_set = TV()
tv_set.turn_on()
tv_set.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])
tv_set.show_channels()
tv_set.show_status()






