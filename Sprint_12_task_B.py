# Id решения 51565799
from collections import Counter


def game(fingers, matrix):
    count = Counter([int(item) for item in matrix])
    score = 0
    for i in range(0, 10):
        if (i in count) and (count[i] <= fingers*2):
            score += 1
    return score


fingers = int(input())
matrix = list((''.join([input() for i in range(4)])).replace('.', ''))

if __name__ == "__main__":
    print(game(fingers, matrix))
