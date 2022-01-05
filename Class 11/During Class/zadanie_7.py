class Message():
    def __init__(self, message):
        self.message = ""

    def set_message(self, message):
        self.message = message[0].upper() + message[1:].lower()

class SMS(Message):
    def __init__(self, sender, recipient, message):
        self.sender = sender
        self.recipient = recipient
        super().set_message(message)

    def send(self):
        print("Sending SMS...")
        print(f"Od: {self.sender} Do: {self.recipient} \n{self.message}")


class Email(Message):
    def __init__(self, senders_address, recipient_address, subject, message):
        self.senders_address = senders_address
        self.recipient_address = recipient_address
        self.subject = subject
        super().set_message(message)

    def send(self):
        print("Sending Email...")
        print(f"Od: {self.senders_address} Do: {self.recipient_address} Temat: {self.subject} \n{self.message}")


s = SMS("123456789", "123456789", "cześć KOLEGO. Co tam u ciebie?")
e = Email("sender@test.pl", "recipient@test.pl", "Jakiś temacik", "cześć KOLEGo. Co tam u ciebie?")
s.send()
e.send()