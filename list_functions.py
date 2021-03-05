lucky_numbers = [483, 829, 153, 1611, 232, 42]
friends = ["Alex", "Max", "Jenny", "Bekey", "John"]

print(friends)

#Apending individual elements to list
friends.append("Lina")
print(friends)

#inserting elements inside of list at a particular position
friends.insert(2,"Obama")
print(friends)

#Apending two lists
friends.extend(lucky_numbers)
print(friends)

#removing from list
friends.remove("Lina")
print(friends)

#removing everything from list
friends.clear()
print(friends)

friends.append("boby")
friends.append("rocky")
friends.append("jenny")

#pop -> removes the last element
friends.pop()
print(friends)

#index of an element in list
print(friends.index("rocky"))

friends.append("rocky")
friends.append("rocky")

#number of occurence of an element in list
print(friends.count("rocky"))

friends.append("livi")
friends.append("appy")
friends.append("biwi")

#sorting list
friends.sort()
print(friends)

lucky_numbers.sort()
print(lucky_numbers)

#reverse a list
lucky_numbers.reverse()
print(lucky_numbers)

#copy of a list
new_friends = friends.copy()
print(new_friends)