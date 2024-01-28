orders = int(input())
total_sum = 0

for i in range(0, orders):
    price = float(input())
    days = int(input())
    capsules = int(input())
    if (price < 0.01 or price > 100) or (days <1  or days > 31) or (capsules < 1 or capsules > 2000):
        continue
    price_sum = 0
    price_sum = price * days * capsules
    total_sum += price_sum
    print(f"The price for the coffee is: ${price_sum:.2f}")

print(f"Total: ${total_sum:.2f}")