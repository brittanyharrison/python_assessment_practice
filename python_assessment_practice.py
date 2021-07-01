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

# def add_value(num1,num2):
#     return num1 + num2
#
# def subtract_value(num1, num2):
#     return num1 - num2
#
# print(add_value(2,4))
# print(subtract_value(4,2))

# Q10. Declare a dict with three shopping items with cost
# egg =.1.20,milk = 2.30,bread = 1.00
# Write a function that returns a total value
# shopping_list = {"eggs": 1.20,
#                  "milk": 2.30,
#                  "bread": 1.00}
#
#
# def total_value(shopping_list):
#     return sum(shopping_list.values())
#
#
# print(total_value(shopping_list))
#
# # Q11. Prompt user to enter an integer.Declare a func that checks if the number is odd or even and display "The n"
#
# number = int(input("Enter a number"))
# def even_odd(number):
#     if number % 2 == 0:
#         print("Your number is even")
#     else:
#         print("Your number is odd.")
# even_odd(number)

# Q12. select the correct syntax
# 1 -super.__init().
# 2- super()__init().
# 3 - super().__init().
# 4 - Super().__init__()

# Q13. Declare a tuple with 3 values. Iterate through the tuple and display the values.
# Cant delete as they are immutable
# this_tuple = (1, 2, 3)
# for numbers in this_tuple:
#     print(numbers)

# Q14 Create student class with mthod called student_data, returns student_name
# clas called devops_student and inherit student class and print name

# class Student:
#     def student_data(student_name):
#         return student_name
#
#
# class DevopsStudent(Student):
#     super().__init__()
#
#
# new_student = DevopsStudent()
# print(new_student.student_data("Brittany"))


# Declare a variable called city, declare a method that takes city as an arg
# and value of the city as London and method checks if value is London

# city = "London"
# def check_city(city):
#     if city == "London":
#         return True
#     else:
#         return False
# print(check_city(city))
