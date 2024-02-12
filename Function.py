# Inbuilt functions
number = max(89, 70, 23, 45, 123)
print(number)

x = min(78, 45, 34, 1)
print(x)

z = pow(2, 3)
print(z)


# User defined functions
def name():
    print("Hillary")


name()  # Calling a function


def student():
    name = "Hillary"
    age = "18"
    course = "MIT"
    print(name, age, course)


student()


# Parameters/variables and arguments

def students(name, age, course):
    print(name, age, course)

students("Hillary",45,"MIT")
students("Hills",15,"MIT")
students("lary",65,"MIT")
students("Ray",45,"MIT")
students("Hillary",45,"MIT")
students("Hilla",45,"MIT")

# Create a user-defined function
def employees(fullname,age,gender,position,salary):
    print(fullname,age,gender,position,salary)

employees("Hillary gangi","18","Male","Manager","100000")
employees("Hills Mwenje","18","Male","Secretary","90000")
employees("Hillary gangi","18","Male","Manager","100000")
employees("Hillary gangi","18","Male","Manager","100000")
employees("Hillary gangi","18","Male","Manager","100000")









