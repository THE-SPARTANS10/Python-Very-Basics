#Functuon without any parameter
def greeting():
    print("Hello user")

#Function with parameter
def para_greeting(name):
    print("Hello " + name)

#Function with more then one parameter
def new_para_greeting(name, age):
    print("Hello " + name + ". You are " + str(age))

greeting()
para_greeting("Max")
new_para_greeting("Mill", 30)
