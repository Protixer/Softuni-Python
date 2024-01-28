number = int(input())

for i in range(0,number):
    numbers = int(input())
    if numbers % 2 != 0:
        print(f"{numbers} is odd!")
        break  
else:
    print(f"All numbers are even.")
