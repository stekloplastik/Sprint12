d = int(input())
temp = list(map(int, input().split()))

temp=[min(temp)-1]+temp+[min(temp)-1]
w_ch=len([n for n in range(1,len(temp)) if temp[n-1]<temp[n] >temp[n+1]])

print(w_ch)
