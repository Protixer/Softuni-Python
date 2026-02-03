pencils = int(input())
markers = int(input())
water = int(input())

sum_all_products = (pencils * 5.8) + (markers * 7.2) + (water * 1.2)
price_with_off = sum_all_products - (sum_all_products * 0.25)

print(price_with_off)