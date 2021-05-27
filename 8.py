number1 = str(input())
number2 = str(input())
intSum = int(number1, 2) + int(number2, 2)
result = bin(intSum)[2:]
print(result)
