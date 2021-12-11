# Contact

class Contact:

    def __init__(self, name, email, telephone):
        self.name = name
        self.email = email
        self.telephone = telephone


    def status(self):
        print(f"\tName: {self.name}")
        print(f"\tEmail: {self.email}")
        print(f"\tTelephone: {self.telephone}")
