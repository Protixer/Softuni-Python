while True:
    command = input()

    if command == 'Welcome!':
        print("Welcome to Hogwarts.")
        break

    if command == 'Voldemort':
        print("You must not speak of that name!")
        break
    
    lenth_command = len(command) 
    
    if lenth_command < 5:
        print(f"{command} goes to Gryffindor.")
    elif lenth_command == 5:
        print(f"{command} goes to Slytherin.")
    elif lenth_command == 6:
        print(f"{command} goes to Ravenclaw.")
    elif lenth_command > 6:
        print(f"{command} goes to Hufflepuff.")
