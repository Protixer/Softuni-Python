"""List Swap"""
# list = ["one", "two", "three", "four", "five", "six"]
# list[3],list[5],list[1] = list[5],list[3], list[0]
# print(list)

""" List Comprehension """
# quote = "life, uh, finds a way"
# print({char for char in quote if char in "aeiou"})
# print([(x, y) for x in [1,2,3] for y in [3,1,4]])
# print([x for x in range(0, 10)])
# print([char for char in quote])

""" List Append"""
# fruits = ["apple","banana","blueberry"]
# fruits.append("nar")
# print(fruits)

""" List Clear """
# fruits = ["apple","banana","blueberry"]
# fruits.clear()
# print(fruits)

""" List Copy """
# fruits = ["apple","banana","blueberry"]
# copy_fruits = fruits.copy()
# print(copy_fruits)

""" List Count """
# fruits = ["apple","banana","blueberry","apple","apple"]
# count = fruits.count("apple")
# print(count)

""" List Extend """
# fruits = ['apple', 'banana', 'cherry']
# cars = ['Ford', 'BMW', 'Volvo']
# fruits.extend(cars)
# print(fruits)
# print(cars)

# fruits = ['apple', 'banana', 'cherry']
# cars = ['Ford', 'BMW', 'Volvo']
# fruits += cars
# print(fruits)

""" List Index """
# valorant_agents = ["Jet", "Reyna", "Viper"]
# print(valorant_agents.index("Reyna"))

""" List Insert """
# valorant_agents = ["Jet", "Reyna", "Viper"]
# valorant_agents.insert(2,"Neon")
# print(valorant_agents)

""" List Pop"""
valorant_agents = ["Jet", "Reyna", "Viper"]
valorant_agents.pop(2)
print(valorant_agents)