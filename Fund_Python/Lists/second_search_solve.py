number = int(input())
word = input()
string_list = []

for n in range(number):
    strings =  input()
    string_list.append(strings)

print(string_list)

for i in range(len(string_list) - 1, -1, -1):
    new_string = string_list[i]
    if word not in new_string:
        string_list.remove(new_string)

print(string_list)