"""
Sample questions to help with the python assessment.
"""


# Q1.Declare a function called username that takes one arg as a string and return the name
# def username(name):
#     return name
# print(username("Brittany"))

# Q2.Declare a list with numbers 1-5. Iterate through the list and display the list
# this_list = [1, 2, 3, 4, 5]
# for number in list:
#     print(number)

# Q3.AND, &&, &, == Which one returns boolean value?
# name = "Brittany"
# if name == "Brittany"

# Q4. What is the difference between list and a tuple
# Lists are mutable and tuples are immutable.

# Q5. Can we add an element to list and tuple?
# List = yes, diff types = yes
# Tuple = yes, diff types = no

# Q6. Create a dict with key value pairs first_name, last_name
# this_dict = {"first_name":"Brittany",
#              "last_name": "Harrison"}

# Q7. Add course to the dictionary
# this_dict = {"first_name":"Brittany",
#              "last_name": "Harrison"}
# this_dict["course"] = "DevOps"
# print(this_dict)

# Q8. Create a class called student. Initialise the class and create and object of that class

# class Student:
#     def __init__(self,name):
#         self.name = name
#
# new_student = Student("Brittany")
# print(new_student.name)

# Q9. Create two func that takes two arguments each. Func1 = add value, Func2 = subtract value

def add_value(num1,num2):
    return num1 + num2

def subtract_value(num1, num2):
    return num1 - num2

print(add_value(2,4))
print(subtract_value(4,2))

