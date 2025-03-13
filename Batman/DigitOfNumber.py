n = 1234

def SumOfDigits(n):
    sum = 0

    while n > 0:
        digit = n % 10
        sum += digit
        n //= 10

    return sum

def OptimizedSumOfDigits(n):
    s = str(n)
    sum = 0
    for i in s:
        sum += int(i)

    return sum

print(OptimizedSumOfDigits(n))