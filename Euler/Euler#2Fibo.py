num1  = 0 
num2 = 1
n = 


summ = 0
while n - 2 > 0 :
    temp = num1
    num1 = num2
    num2 = temp + num1
    if num2 % 2 == 0: 
        summ += num2
    n -= 1

print(summ)

# def fib(n):
#     if n == 0:
#         return 0
    
#     if n == 1:
#         return 1
    
#     else:
#         return fib(n - 1) + fib(n - 2)
    
# print(fib(5 - 1))