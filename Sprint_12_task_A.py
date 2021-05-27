# Id решения 51564953
def nearest_zero(length, street_numbers):
    infinity = 10 ** 9
    result = [infinity] * length
    large = infinity
    for i in range(length):
        if not street_numbers[i]:
            large = 0
        result[i] = min(result[i], large)
        large += 1

    large = infinity
    for i in range(length - 1, -1, -1):
        if not street_numbers[i]:
            large = 0
        result[i] = min(result[i], large)
        large += 1
    return ' '.join(map(str, result))


length = int(input())
street_numbers = list(map(int, input().split()))

if __name__ == "__main__":
    print(nearest_zero(length, street_numbers))
