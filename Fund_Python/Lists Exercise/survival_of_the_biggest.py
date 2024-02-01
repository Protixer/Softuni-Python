""" First option"""
# text = input().split(' ')
# text = [int(i) for i in text]

# n = int(input())
# deleted_items = []

# for i in range(0,n):
#     min_number = min(text)
#     deleted_items.append(min_number)
#     text.remove(min_number)

# text = ", ".join(str(el) for el in text)
# print(text)

""" Second option"""
text = input().split(' ')
text = [int(i) for i in text]

n = int(input())

for i in range(0,n):
    min_value = text[0]
    for j in range(0, len(text)):
        if min_value > text[j]:
            min_value = text[j]

    text.remove(min_value)

text = ", ".join(str(el) for el in text)
print(text)