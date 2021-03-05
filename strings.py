print("This is a string")

#Escape sequence
print("This is a\nnew line")

#including " in string
print("this is a \"quotation mark\"")

#Creating string variable
greeting="Hey there"
print(greeting)

#String concatination
greeting+=", how are you?"
print(greeting)

#Functions of string
name="I AM SUPRATIM"
print(name.lower())

name="i am supratim"
print(name.upper())

print(name.islower())
print(name.isupper())

name="I AM SUPRATIM"

print(name.isupper())
print(name.islower())

name = "I aM SuPrAtim"
print(name.isupper())
print(name.islower())

print(len(name))

#Indexes
text="ABCDEFG"
    # 01234567
    # -8-7-6-5-4-3-2-1 
print(text[0],end=" ")
print(text[3],end=" ")
print(text[6],end=" ")
print(text[-2])

print(text.index("C"))
print(text.index("DEF"))

#replacing part of string
text=text.replace("ABC","XYZ")
print(text)