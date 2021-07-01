# Python Assessment Practice 

### Topics to cover:

-[x] How can you inherit a class from x to y

```python
# Create a 'Student' class and 'DevopsStudent' class that inherits 'Student' class
class Student:
 def student_name(self,name):
  return name 

class DevopsStudent(Student):
 def __init__(self):
  super().__init__()
 
 new_student = DevopsStudent()
 new_student.student_name("Brittany")

```
  
-[x] Collections - Lists - Tuples - Sets - Dictionary
```python
# Create a List, Tuple, Set and Dictionary 
my_list = ["eggs","milk", "cheese", 1.90, 2.30, 4.00] # Mutable and contain different data types
my_tuple = ("eggs","milk", "cheese",1.90, 2.30, 4.00) # Immutable and can contain diff data type
my_set = {"eggs", "milk", "cheese", 1.90, 2.30,4.00} # Immutable, unordered, unindexed, no duplicates,contain diff data types
my_dict = {"eggs":1.90, "milk":2.30, "cheese":4.00} # Mutable, no duplicates
```

-[x] Syntax related - how to declare a dictionary
```python
# Declare shopping_list dictionary and prices
my_dict = {"eggs":1.90, "milk":2.30, "cheese":4.00}
# Print "milk" value of my_dict
print(my_dict["milk"])
# Find length of my_dict
len(my_dict)
# Use method to return list of all the keys in my_dict
x = my_dict.keys()
# Change values
my_dict["cheese"] = 3.40
# Add items
my_dict["coffee"] = 4.80
# Remove item
my_dict.pop("cheese") # or
del my_dict["cheese"]
# loop through key and value in my_dict
for x, y in my_dict.items():
    print(x,y)
```
 
-[x] What is the difference between function and method

- `Function: block of code that carry out a specific task`
 
- `Method: A method in python is somewhat similar to a function, except it is associated with object/classes.`
  - `The method is implicitly used for an object for which it is called.`
  - `The method is accessible to data that is contained within the class.`
 
-[x] Methods/functions declaration syntax
```python
# Function syntax
def function_name(arg1,arg2...):
   # function body

# Method syntax
class ClassName:
    def method_name():
    # method body
```

-[ ] Control flow - if - elif - else
```python
# Create a control flow 
a = 2
b = 4
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else:
    print("a is equal to b")
```
 
-[ ] Loops - for loop and while loop - syntax for records in row:
 ```python

```
-[ ] Operators - conditional operators - Boolean - maths related
 
-[ ] Built in methods - dict = [4,5,6,7,8] - add a 5 at the end of this list - indexing
 
-[ ] OOP - Inheritance - Encapsulation - Polymorphism - abstraction (how to implement them)
 
-[ ] Keywords and use cases self - super - __init__()
 
-[ ] Syntax to declare a class with super __init__() - _init() -
 
-[ ] declare 4 methods that take 4 arguments - no class is needed - specific functionality - method to return % of the 
 2 values give 
