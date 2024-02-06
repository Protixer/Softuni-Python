""" Repeating String with lambda"""

# string = input()
# n = int(input())

# repeat_string = lambda a, b: a * b
# string = repeat_string(string, n)
# print(string)

""" Repeating string with multiply"""

# string = input()
# n = int(input())
# print(string * n)


""" String repeating with function """


def repeat_string(string, times):
    return string * times


string = input()
n = int(input())
print(repeat_string(string, n))
