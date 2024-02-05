string = input()
n = int(input())

repeat_string = lambda a, b: a * b
string = repeat_string(string, n)
print(string)
