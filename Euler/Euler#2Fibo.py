# num1  = 0 
# num2 = 1
# n = 5

# print(num1 , end= " ")
# print(num2 , end= " ")


# while n - 2 > 0 :
#     temp = num1
#     num1 = num2
#     num2 = temp + num1
#     print(num2, end= " ")
#     n -= 1

def recursion(n):
    if n == 0:
        return 0
    
    if 