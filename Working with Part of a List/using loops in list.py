name=["rohan","sushma","alok","sunny","satyarth"]
for i in name:
    print(i.title())

# we can also do like this

print("\n printing only first three names in the list")

for i in name[0:3]:
    print(i.title())

for i in range(0,3):
    print(name[i].title())