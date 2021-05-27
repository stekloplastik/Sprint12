a, b, c = map(int, input().split())

list=[a,b,c]
n=0

for i in list:
    if i % 2 ==0:
        n+=1
    else:
        n-=1

if n ==3 or n==-3:
    print('WIN')
else:
    print('FAIL')