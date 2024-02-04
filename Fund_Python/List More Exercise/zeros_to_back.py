text = [int(x) for x in input().split(", ")]
zero_element = 0
for i in range(0, len(text)):

    if text[i] == 0:
        text.remove(text[i])
        text.append(zero_element)

print(text)
