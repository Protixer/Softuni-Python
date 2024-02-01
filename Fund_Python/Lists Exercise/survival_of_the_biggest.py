text = input().split(' ')
text = [int(i) for i in text]

n = int(input())
deleted_items = []

for i in range(0,n):
    min_number = min(text)
    deleted_items.append(min_number)
    text.remove(min_number)

print(type(text))
text = ", ".join(str(el) for el in text)
print(text)