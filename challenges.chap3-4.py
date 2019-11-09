
"""THIS IS CHAPTER 3 !!!!"""


# challenge 1




# my strings

print("Hey")
print("How")
print("Are You")


# teacher's strings


print("Above")
print("and")
print("beyond")



# challenge 2



# my if else

x = 50

if x < 10:
    print ("you are small")
elif x >= 10:
    print ("you are big")
else:
    print ("nothing")





# the teacher's program


x = 11
if x < 10:
    print("x is less than 10.")
else:
    print("x is greater than or equal to 10")





# challenge 3


# my original code mistake

x = 50

if x <= 10:
    print("you suck")
elif x > 10,  <= 25:
    print("you rock!!!")
elif x > 25:
    print("dream big")
else:
    print("nada")


    """I thought I had to put a coma after the(x >, <=25)"""

"""that was a mistake and the program would already print a message if the program is
 greater than ten, if it wasn't then the 1st message would print anyway, because of: if x <= 10"""



# my improved code:



x = 50

if x <= 10:
    print("you suck")
elif x <= 25:
    print("you rock!!!")
elif x > 25:
    print("dream big")
else:
    print("nada")




# teach's code:


x = 2

if x <= 10:
    print("x is less than or equal to 10.")
elif x <= 25:
    print("x is greater than 10, but less than or equal to 25.")
else:
    print("x is greater than 25.")




# challenge 4

# my code


x = 9
z = 2


print (x % z)


# teach's code:


100 % 13






# challenge 5

"""---------"""

# my code

x = 25
y = 5


print(x / y)


# teach code:

100 // 4


# challenge 6

"""----------"""

# mine:


age = 2

if age == 3:
    print("my baby's getting big")
elif age < 3:
    print("My baby")
else:
    print("newborn")



# teach:

age = 64
retirement = age - 65

if retirement < 10:
    print("You get to retire soon.")
else:
    print("You have a long time until you can retire!")


#----#-------#------#----#----------#---------#

"""THIS IS CHAPTER 4 !!!!!"""

Challenge 1

# my code

x = 2

def f(x):
    return x ** 2


result = f(x)
print(result)





# teach's code


def squared(x):
    return x ** 2

print(squared(2))






Challenge 2


# my code mistake


def hard_code(string):
    return("hello, world")
         




result = hard_code()
print(result)




# my code



def hard_code(code):
    print(code)


hard_code("I am confused")




# teacher code



def print_string(string):
    print(string)

print_string("Testing: 1, 2, 3.")







Challenge 3

# my code:


def mult(x, y, z):
    return x * y * z


x = 10
y = 8
z = 4


result = mult(x, y, z)
result = mult(20)
print(result)


"""it won't run for some reason"""



# teach's code


def add_mult(a,b,c,x=100,z=1000):
    return a + b + c * x * z

result = add_mult(10, 15, 25)
print(result)






Challenge 4

# my code


def f(x=4):
    return x / 2


result = f(4)
print(result)




def add(p=8):
    return p * 4




result = add()
print(result)


"""----------"""


# teach code


def divide(x):
    return x / 2


def multiply(x):
    return x * 4

y = divide(4)
z = multiply(y)

print(z)





Challenge 5

# my code

float("100")







#teach code


def convert(string):
    try:
        return float(string)
    except ValueError:
        print("Could not convert the string to a float.")

c = convert("55.0")
print(c)





Challenge 6


# my code

"""wrote a prgramm where the parameter was squared"""


x = 2

def f(x):
    return x ** 2


result = f(x)
print(result)







"""Passed a string as a pamameter in a function"""


def hard_code(code):
    print(code)


hard_code("I am confused")




"""passed three required parameters and two optional ones"""



def mult(x, y, z):
    return x * y * z


x = 10
y = 8
z = 4


result = mult(x, y, z)
result = mult(20)
print(result)

"""defined two different functions and printed the results """



def f(x=4):
    return x / 2


result = f(4)
print(result)




def add(p=8):
    return p * 4






"""converts the string 100 to a floating point number"""

float("100")






# teach code

def squared(x):
    """ Takes an int and returns it multiplied by 2.
    :param x: int.
    :return: x multiplied by 2.
    """
    return x ** 2


def print_string(string):
    """ Prints the string passed in.
    :param string: str.
    """
    print(string)

print_string("Testing: 1, 2, 3.")


def add_mult(a,b,c,x=100,z=1000):
    """ Returns the result of two optional params
    multiplied by the addition of 3 required params.
    :param a: int.
    :param b: int.
    :param c: int.
    :param x: int.
    :param z: int.
    :return: int.
    """
    return a + b + c * x * z


def convert(string):
    """ Converts passed in str to int.
    :param string: str.
    :return: string converted to int.
    """
    try:
        return float(string)
    except ValueError:
        print("Could not convert the string to a float.")







    




