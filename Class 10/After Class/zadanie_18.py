# Zadanie 18

class Account:

    def __init__(self, number):
        self.number = number
        self.balance = 0


    def status(self):
        print("Status:")
        print(f"\tBank Account No: {self.number}")
        print(f"\tBalance: PLN {self.balance}")


    def cash_in(self, n):
        self.balance = self.balance + n
        print(f"Operation: - {n}")


    def cash_out(self, n):
        if self.balance - n >= 0:
            self.balance = self.balance - n
            print(f"Operation: + {n}")
        else:
            print(f"Insufficient funds on the account!")


# g
a1 = Account("12 3456 5555 9090 1111 0000 7722")
# h
a1.status()
# i
a1.cash_in(25.30)
# j
a1.status()
# k
a1.cash_out(31.70)
# l
a1.status()
# m
a1.cash_out(14)
# n
a1.status()