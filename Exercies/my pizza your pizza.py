mypizza=["pepperoni","mushrooms","green peppers","extra cheese"]
friendpizza=mypizza[:]

print("My favorite pizzas are:  ")
for pizza in mypizza:
    print(pizza)

print("\n my firends faviorite pizzas are:")
for pizza in friendpizza:
    print(pizza)

mypizza.append("apple pizza")
friendpizza.append("banana pizza")

print("\n my new list of favorite pizzas are: ")
for pizza in mypizza:
    print(pizza)
print("\n my friends new list of favorite pizzas are: ")
for pizza in friendpizza:
    print(pizza)