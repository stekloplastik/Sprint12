from string import punctuation, whitespace

text = str(input())

for p in punctuation:
    if p in text:
        text = text.replace(p, '')

for p in whitespace:
    if p in text:
        text = text.replace(p, '')

text = text.lower()       

if text == text[::-1]:
    print('True')
else:
    print('False')
