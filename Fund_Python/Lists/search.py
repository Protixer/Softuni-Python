n = int(input())
key_word = input()
unfiltered_list = []
list_contains_text_softuni = []

for _ in range (0,n):
    text = input()

    if key_word in text:
        list_contains_text_softuni.append(text)
    
    unfiltered_list.append(text)

print(unfiltered_list)
print(list_contains_text_softuni)