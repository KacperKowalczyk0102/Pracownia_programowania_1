# Zad 14
print("\nZadanie 14")

###
# Obliczanie powierzchni i obwodu koła
###

# określ promień i PI
r = 5
import math
pi = math.pi

# obliczyć obszar
pole = round(pi*(r**2), 2)

# oblicz obwód
obw = round(2*pi*r, 2)

# wyświetl wyniki
print("Pole koła = ", pole)
print("Obwód koła = ", obw)
