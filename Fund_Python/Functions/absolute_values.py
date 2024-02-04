""" Option one"""

# list_of_values = [abs(float(x)) for x in input().split()]
# print(list_of_values)

""" Option two"""
list_of_values = input().split()


def absolute_value(list_of_values):
    new_list = []
    for i in range(0, len(list_of_values)):
        list_of_values[i] = abs(float(list_of_values[i]))
        new_list.append(list_of_values[i])

    return new_list


print(absolute_value(list_of_values))
