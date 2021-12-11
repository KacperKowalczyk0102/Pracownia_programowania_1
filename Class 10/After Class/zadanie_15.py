# Zadanie 15

class TV:

    def __init__(self):
        self.is_on = False;
        self.channel_on = 1;
        self.channels_list = [];
        self.volume = 0;


    def turn_on(self):
        self.is_on = True


    def turn_off(self):
        self.is_on = False


    def show_status(self):
        print("Status:")
        if self.is_on == True:
            print(f"\tTV is on")
            if len(self.channels_list[self.channel_on - 1]) > 0:
                print(f"\tChannel: {self.channel_on} ({self.channels_list[self.channel_on-1]})")
            else:
                print(f"\tChannel: {self.channel_on}")
            print(f"\tVolume: {self.volume}")
        else:
            print("\tTV is off")


    def new_channel(self, new_channel_on):
        self.channel_on = new_channel_on


    def set_channels(self, channels_list):
        self.channels_list = channels_list


    def show_channels(self):
        print("Channels list: ")
        if len(self.channels_list) > 0:
            for k, n in enumerate(self.channels_list):
                print(f"\t{k + 1}. {n}")
        else:
            print("\tEmpty")


    def volume_down(self):
        if self.volume > 0:
           self.volume = self.volume - 1;

        if self.volume == 00:
            print(f"Volum level: {self.volume} (min)")
        else:
            print(f"Volum level: {self.volume}")


    def volume_up(self):
        if self.volume < 10 :
            self.volume = self.volume + 1;

        if self.volume == 10:
            print(f"Volum level: {self.volume} (max)")
        else:
            print(f"Volum level: {self.volume}")


tv_set = TV()
tv_set.turn_on()
tv_set.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])
tv_set.volume_down()
tv_set.volume_up()
tv_set.show_channels()
tv_set.show_status()






