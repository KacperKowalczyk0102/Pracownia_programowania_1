# Coontact list

from contact import Contact

class Contact_list():

    def __init__(self):
        self.contacts = []


    def add_new(self, name, email, telephone):
        c1 = Contact("John Brown", "brown@onet.pl", "555234000")
        self.contacts.append(c1)


    def display(self):
        lp = 1
        for x in self.contacts:
            print(f"Kontakt {lp}")
            print(x.status())
            lp = lp + 1
