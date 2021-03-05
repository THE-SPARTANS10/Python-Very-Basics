try:
    value=10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as zerr:
    print("Divided by zero")
    print(zerr)
except ValueError as verr:
    print("Invalid input")
    print(verr)
