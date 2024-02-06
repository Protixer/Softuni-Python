def total_price(product, quantity):

    final_price = 0

    if product == "coffee":
        final_price = quantity * 1.50
    elif product == "water":
        final_price = quantity * 1
    elif product == "coke":
        final_price = quantity * 1.4
    elif product == "snacks":
        final_price = quantity * 2

    return final_price


product = input()
quantity = int(input())
final_price = total_price(product, quantity)
print(f"{final_price:.2f}")
