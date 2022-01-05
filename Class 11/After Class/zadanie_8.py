class Phone():
    def __init__(self, number, owner):
        self.number = number
        self.is_lock = True
        self.owner = owner

    def change_status(self):
        if self.is_lock == True:
            self.is_lock = False
        else:
            self.is_lock = True
        print(self.owner)
        print(f"Lock: {self.is_lock}")

    def call(self, who):
        print("Calling ....")
        print(f"To: {who}")
        print(f"From: {self.number}")


p1 = Phone("1236456789", "Michał")
p2 = Phone("987654321", "Mateusz")
p1.change_status()
p2.change_status()
p1.call("Andzia")
p1.call("Julia")

