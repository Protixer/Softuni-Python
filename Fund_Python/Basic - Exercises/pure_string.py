n = int(input())

for i in range(n):
    string = input()
    for elem in string:
        if elem == ',' or elem == '.' or elem == '_':
            print(f"{string} is not pure!")
            break
    else:
        print(f"{string} is pure.")