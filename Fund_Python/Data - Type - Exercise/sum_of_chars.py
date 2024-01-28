num_range = int(input())
result = 0

for _ in range(0, num_range):
    char = input()
    char = ord(char)
    result += char

print(f"The sum equals: {result}")