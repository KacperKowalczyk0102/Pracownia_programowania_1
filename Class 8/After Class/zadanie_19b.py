# Zadanie 19

stos = []
operatory = {'+','-','*','/','%','^'}
liczby = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

text = "23+="
for n in text:

        if n in operatory and len(stos)>=2:
            x = stos.pop()
            y = stos.pop()

            result = 0
            if n == "+":
                result = y + x
            elif n == "-":
                result = y - x
            elif n == "*":
                result = y * x
            elif n == "/":
                result = int(y / x)
            elif n == "%":
                result = y % x
            elif n == "^":
                result = y ^ x

            stos.append(result)

        elif n in liczby:
            stos.append(int(n))

        print(stos)
