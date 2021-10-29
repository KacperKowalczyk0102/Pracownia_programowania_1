# Zadanie 12

def sum(n):

    # 0! = 1, 1! = 1
    if n==0 or n==1:
        return 1

    # n! = n * (n-1)!
    if n > 1:
        return n * sum(n-1)
  
n = 10
print( f"{sum(n)}" )

