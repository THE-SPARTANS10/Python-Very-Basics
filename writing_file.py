
#Appending data to existing file
employee_data=open("dataset.txt" ,"a")
employee_data.write("\nJohn -> 235")
employee_data.write("\nKelly -> 458")
employee_data.write("\nMichi -> 876")

employee_data.close()

#Overwriting a file
employee_data = open("dataset.txt", "w")
employee_data.write("Just Overwrited the whole file")

employee_data.close()
