"""List Swap"""

list = ["one", "two", "three", "four", "five", "six"]

list[3],list[5],list[1] = list[5],list[3], list[0]

print(list)