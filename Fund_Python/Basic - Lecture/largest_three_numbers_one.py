dict = []

for _ in range(0,3):
    a = int(input())
    dict.append(a)

largest_number = -100000000000000000000000000000000000000000

for elem in range(len(dict)):
    if dict[elem] >= largest_number:
        largest_number = dict[elem]

print(largest_number)