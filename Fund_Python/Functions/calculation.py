def multiply(num_one, num_two):
    return num_one * num_two


def divide(num_one, num_two):
    return int(num_one / num_two)


def add(num_one, num_two):
    return num_one + num_two


def subtract(num_one, num_two):
    return num_one - num_two


command = input()
number_one = int(input())
number_two = int(input())

if command == "multiply":
    print(multiply(number_one, number_two))
elif command == "divide":
    print(divide(number_one, number_two))
elif command == "add":
    print(add(number_one, number_two))
elif subtract == "subtract":
    print(subtract(number_one, number_two))
