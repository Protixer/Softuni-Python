text = [int(x) for x in input().split(", ")]
print(text)
zero_element = 0
for i in range(0, len(text) - 1):

    if text[i] == 0:
        text.remove(text[i])
        text.append(zero_element)
        # print("yes")

print(text)
