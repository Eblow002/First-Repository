#Ethan Blow
#2.6.19
#4.13.3: Greeting

name = input("What is your name: ")

def greeting():
    print("Hi there " + name + "!")
    print("Nice to meet you")

greeting()


#4.13.4: Functions and Variables
#Ethan Blow
#2.14.19

x = 11

def print_something():
    x = 13
    print (x)

print_something()
print (x)


#4.13.5: Functions and Variables pt 2
#Ethan Blow
#2.14.19

my_variable = 74.7549278567

def something():
    print(my_variable)

something()



# 4.13.6: Functions and Variables, Part 3
# Ethan Blow
# 2.18.19


def print_number(x):
    print(str(x))

print_number(12)
print_number('\n' + "Hi")


#4.14.4: Name and Age
#Ethan Blow
#2.18.19

def name_and_age(name, age):
    print('Hi, my name is, What? My name is, Who? my name is ',name,' and I am ',str(age),' Years old.')

name_and_age('slica slica slim shady',46)
name_and_age('Dr. Seuss',22)
name_and_age('Ethan Blow',14)


