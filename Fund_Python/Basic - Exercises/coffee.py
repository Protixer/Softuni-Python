sum_coffee = 0
while True:
    command = input()

    if command == 'END':
        break

    if command == 'dog' or command == 'cat' or command == 'coding' or command == 'movie':
        sum_coffee += 1
    elif command == 'DOG' or command == 'CAT' or command == 'CODING' or command == 'MOVIE':
        sum_coffee += 2
    
if sum_coffee > 5:
    print("You need extra sleep")
else:
    print(sum_coffee)