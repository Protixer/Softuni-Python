metars = float(input())
all_yards = metars * 7.61
sum_after = all_yards * 0.18

print(f"The final price is: {(all_yards - sum_after)} lv.")
print(f"The discount is: {all_yards - (all_yards - sum_after)} lv.")