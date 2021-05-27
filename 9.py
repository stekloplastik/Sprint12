n = int(input())
# i = 1
# ans = ''

# while i < n:
#     i = i*4
#     if i == n:
#         ans = 'True'
#     else:
#         ans = 'False'

# print(ans)

def isPowerOfFour(n):
    if (n == 0):
        return False
    while (n != 1):
            if (n % 4 != 0):
                return False
            n = n // 4
    return True

if isPowerOfFour(n):
    print('True')
else:
    print('False')
