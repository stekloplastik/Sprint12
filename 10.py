# def factorize(n):
#     divisor = 2
#     while divisor ** 2 <= n:
#         if n % divisor == 0:
#             n //= divisor
#             print(divisor)
#         else:
#             divisor += 1
#     if n != 1:
#         print(n)

# n = int(input())
# factorize(n)

n = int(input())

def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans

print(Factor(n))