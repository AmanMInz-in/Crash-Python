# Store the locations in a list. Make sure the list is not in alphabetical order.
locations=['Europe', 'Asia', 'Africa', 'Antarctica']
# Print the list in its original order. Don’t worry about printing it neatly, just print it as a raw Python list.
print(locations)
# Use sorted() to print your list in alphabetical order without modifying the actual list.
print("printing the using shorted() function")
print(sorted(locations))

# Show that your list is still in its original order by printing it.
print("printing the orignal list")
print(locations)
# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print("printing the using shorted() function in reverse order")
print(sorted(locations, reverse=True))
# Show that your list is still in its original order by printing it again.
print("printing the orignal list")
print(locations)
# Use reverse() to change the order of your list. Print the list to show that its order has changed.
print("printing the using reverse() function")
locations.reverse()
print(locations)
# Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
print("printing the using reverse() function again")
locations.reverse()
print(locations)
# Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
print("printing the using sort() function") 
locations.sort()
print(locations)
# or we can do
print(sorted(locations))
# Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
print("printing the using sort() function in reverse order")
locations.sort(reverse=True)
print(locations)
# use sort() to change your list so its storedin reverse alphabetical order print the list show that its order has changed
print("printing the using sort() function in reverse order again")
locations.sort(reverse=True)
print(locations)