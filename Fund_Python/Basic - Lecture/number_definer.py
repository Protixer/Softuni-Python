number = float(input())
flag = ""

if number == 0:
    print("zero")

if number > 0:
    flag = "positive"

if number < 0:
    flag = "negative"

if 0 < abs(number) < 1 :
    print(f"small {flag}")
elif abs(number) > 1000000:
    print(f"large {flag}")
else:
    print(flag)

