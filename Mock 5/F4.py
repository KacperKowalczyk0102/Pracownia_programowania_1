# F4

def coins(price):
    ile = 0
    while price > 0:
        if price >= 5:
            price -= 5
            ile += 1
        elif price >= 2:
            price -= 2
            ile += 1
        elif price >= 1:
            price -= 1
            ile += 1
        else:
            continue

    print(ile)
