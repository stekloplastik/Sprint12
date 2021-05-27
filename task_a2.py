# import numpy as np

# n = int(input())
# lst = list(map(int, input().split()))

# def func(lst):
#     #lst=np.array(list(map(int, lst.split())))
#     zeros = np.where(lst==0)[0]
#     for i in np.nonzero(lst)[0]:
#         lst[i] = min(np.abs(i-zeros))
#     return lst.tolist()

# func(lst)
 
def nearest_zero(length, street_numbers):
    infinity = 10 ** 9
    result = [infinity] * length
    l = infinity
    for i in range(length):
        if not street_numbers[i]:
            l = 0
        result[i] = min(result[i], l)
        l += 1
 
    l = infinity
    for i in range(length - 1, -1, -1):
        if not street_numbers[i]:
            l = 0
        result[i] = min(result[i], l)
        l += 1
    return ' '.join(map(str, result)) 


length = int(input())
street_numbers = list(map(int, input().split()))       

if __name__ == "__main__":    
    print(nearest_zero(length, street_numbers))