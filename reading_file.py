#        modes ->
#        "r" -> Read
#        "w" -> Write
#        "a" -> append
#        "r+" -> Read and write

employee_file = open("dataset.txt", "r")
print("Is this file readable? " +  str(employee_file.readable()))

#Reading line by line using cursor
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readline())

#Reading whole file in one go
print(employee_file.read())

employee_file.close()
