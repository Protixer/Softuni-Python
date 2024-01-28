import math 

people = int(input())
capacity = int(input())
result = 0

if people % capacity == 0:
    result = math.ceil(people / capacity)
else:
    result = int(people / capacity) + 1
    
print(result)

