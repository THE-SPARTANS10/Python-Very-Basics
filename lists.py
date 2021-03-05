friends = ["Alex","Max","Jenny","Bekey","John"]
    #index  0      1       2        3      4
#back index -5    -4      -3       -2     -1
print(friends)

#index
print(friends[2])
print(friends[-2])

#slicing
print(friends[1:])
print(friends[:3])
print(friends[1:4])

#changing value
friends[2]="Mike"
print(friends[2])