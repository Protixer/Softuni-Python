count_numbers = int(input())

list_positive = []
list_negative = []

for _ in range(0,count_numbers):
    num = int(input())
    if num >= 0:
        list_positive.append(num)
    elif num < 0:
        list_negative.append(num)

print(list_positive)
print(list_negative)
print(f"Count of positives: {len(list_positive)}")
print(f"Sum of negatives: {sum(list_negative)}")