martrix=[
    [1,2,5,6],
    [5,9,1,5],
    [5,3,1,8]
]

print(martrix[0][3])
print(martrix[1][2])
print(martrix[2][0])
print()

print("All elements are: ")
for row in martrix:
    for element in row:
        print(element, end=" ")
    print()
    
