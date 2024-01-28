while True:
    string = input()
    if string == 'End':
        break
    word = ''
    for i in range(0, len(string)):
        word += (string[i] + string[i])
    if string != 'SoftUni':
        print(word)
    else:
        continue