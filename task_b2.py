from collections import Counter

k = 1

matrix = ''.join([input() for i in range(4)])

print(matrix)

print(type(matrix))
nm = matrix.replace('.','')

m = list(nm)
print(m)
result = [int(item) for item in m]
print(result)

cnt = Counter(result)

print(cnt)

score = 0

for i in range(0, 10):
    if (i in cnt) and (cnt[i] <= k*2):
        score +=1 

print(score)