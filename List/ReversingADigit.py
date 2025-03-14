n = 1467080

def Reverse(n):
    rev_n = 0
    while n:
        digit = n % 10
        rev_n += digit
        rev_n *= 10
        n //= 10

    return rev_n

def OptimizedRev(n):
    return str(n).rstrip("0")[::-1]


print(OptimizedRev(n))