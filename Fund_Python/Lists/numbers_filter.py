number = int(input())
numbers_list = []
filter_list = []

for n in range(number):
    num = int(input())
    numbers_list.append(num)

command = input()

for number in numbers_list:
    if command == 'even' and number % 2 == 0:
        filter_list.append(number)
    elif command == 'odd' and number % 2 != 0:
        filter_list.append(number)
    elif command == 'negative' and number < 0:
        filter_list.append(number)
    elif command == 'positive' and number  >= 0:
        filter_list.append(number)

print(filter_list)