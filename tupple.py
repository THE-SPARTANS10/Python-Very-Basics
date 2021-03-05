#important -> tupples are immutable
#They are mainly immutable list
#we will use tupples when we want to store data which we will not edit
coordinates = (4,5,6)
print(coordinates)
print(coordinates[0])
print(coordinates[1])
print(coordinates[2])

#you can't do coordinates[1] = 7, this will give us error

#list of tupples
data = [(2,8), (5,9), (6,7)]
print(data[1])
print(data[0][1])