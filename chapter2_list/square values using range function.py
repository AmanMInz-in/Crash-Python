from operator import add


squares=[]
for value in range(1,11):
    square= value**2
    squares.append(square)
print(squares)

# now i am creating a program if i adding a list in a range

ad=[]
for value in range(1,11):
    some= add(value,value)
    ad.append(some)
print(ad)

# no we can use sum function to add the values present in the list

total=sum(ad)
print(total)