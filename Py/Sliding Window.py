import math


str1 = "ABCdABCd"
str2 = "ABCd"


if str1 + str2 != str2 + str1:
    print("")
max_length = math.gcd(len(str1), len(str2))
print (str1[:max_length])