n = 1467

def Reverse(n):
    rev_n = 0
    while n > 0:
        digit = n % 10
        rev_n += digit
        rev_n *= 10
        n //= 10

    return rev_n

print(Reverse(n))