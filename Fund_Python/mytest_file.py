"""List Swap"""

# list = ["one", "two", "three", "four", "five", "six"]

# list[3],list[5],list[1] = list[5],list[3], list[0]

# print(list)

""" List Comprehension """
quote = "life, uh, finds a way"
print({char for char in quote if char in "aeiou"})

print([(x, y) for x in [1,2,3] for y in [3,1,4]])

print([x for x in range(0, 10)])

print([ char for char in quote])