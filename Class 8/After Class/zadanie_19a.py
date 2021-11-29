# Zadanie 19

stos = []
operatory = {'+','-','*','/','%','^'}
liczby = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

def start(data):

        if data in operatory and len(stos)>=2:
            x = stos.pop()
            y = stos.pop()

            result = 0
            if data == "+":
                result = y + x
            elif data == "-":
                result = y - x
            elif data == "*":
                result = y * x
            elif data == "/":
                result = int(y / x)
            elif data == "%":
                result = y % x
            elif data == "^":
                result = y ^ x

            stos.append(result)

        elif data in liczby:
            stos.append(int(data))

        print(stos)
        # print(wyjscie)
        data = input("Kolejny znak: ")
        if data != "=":
            start(data)
        else:
            print(f"Wynik: {stos.pop()}")


data = input("Kolejny znak: ")
start(data)