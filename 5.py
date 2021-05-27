n = int(input())
l = str(input())
word = ''
for i, item in enumerate(l.split()):
    if len(word) < len(item):
        word = item
print(word)
print(len(word))
