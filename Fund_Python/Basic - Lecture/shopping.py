budget = int(input())

while True:
    element = input()

    if element == 'End':
        print('You bought everything needed.')
        break
    if int(element) > budget:
        print("You went in overdraft!")
        break
    budget -= int(element)
else:
    print("You bought everything needed.")