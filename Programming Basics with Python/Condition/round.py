hours = int(input())
minutes = int(input())

hours_to_minutes = hours * 60 + minutes + 15

print(f"Time after 15 minutes: {int(hours_to_minutes / 60)}:{int(hours_to_minutes % 60)}")

if hours_to_minutes % 60 < 10:
    print(f"Time after 15 minutes: {int(hours_to_minutes / 60)}:0{int(hours_to_minutes % 60)}")
if hours_to_minutes / 60 >= 24:
    print(f"Time after 15 minutes: 0:{int(hours_to_minutes % 60)}")

