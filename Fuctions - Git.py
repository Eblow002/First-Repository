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


# 4.14.5: Default Parameter Values
# Ethan Blow
# 2.19.19

def print_2_numbers(x,y = 20):
    print('First Number: ',x)
    print('Second Number: ',y)

print_2_numbers(5, 67)
print_2_numbers(23)


# 4.14.7: Print multiple times
# Ethan Blow
# 2.19.19

def print_multiple_times(string, times):
    for i in range(times):
        print(string)

print_multiple_times('Whats up my dude',101)


# 4.14.7: Print multiple times
# Ethan Blow
# 2.19.19

def print_multiple_times(string, times):
    for i in range(times):
        print(string)

print_multiple_times('Whats up my dude',101)


# 4.16.3: Enter a number
# Ethan Blow
# 2.20.19

try:
    my_number = int(input('Enter a integer '))
    print('Your number: ' + str(my_number))

except ValueError:
    print('That was not a integer')


<<<<<<< HEAD
# 4.16.4: Enter name and age
# Ethan Blow
#2.20.19

name = input('What is your name: ')

age = -1

try:
    age = int(input('Enter your age: '))

except ValueError:
    print('Pretty sure that was not a number')

print('\n''Name: ',name)
print('Age: ',age)
=======
# 4.16.6: Temprature Converter
# Ethan Blow
# 2.20.19

def c_to_f(c):
    return c * 1.8 + 32

def f_to_c(f):
    return (f - 32) / 1.8

try:
    c = float(input('Enter a temp in C: '))
    print('In F: ',round(c_to_f(c), 2))

    f = float(input('Enter a temp in F: '))
    print('In C: ',round(f_to_c(f), 2))

except ValueError:
    print('You must enter a float')
>>>>>>> Temp-Converter
