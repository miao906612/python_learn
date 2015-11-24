# -*- coding: utf-8 -*-
#########################################################################
# File Name: dynamicTyping.py
# Author: Shuo Miao
# mail: miao906612@163.com
# Created Time: 2015年11月24日 13:09:03
#########################################################################

#Dynamic Typing Model

#In python,types are determined automatically at runtime, not in response
#to declarations in your code.

#Variables, Objects and References

#Four points for Variables
#1 Variables are entries in a system table, with spaces for links to 
#  objetcs
#2 Variable creation---A variable( i.e. name) is created when your code
#  first assigns it to a value. Future assignments change the value of 
#  the already created name. Technically, Python detects some names 
#  before your code runs.
#3 Variable types---A variable never has any type information or
#  constraints associated with it. The notion of type lives with objects.
#  Variables are generic in nature; they always simply refer to a 
#  particular object at a particular point in time
#4 Variable use---When a variable appears in an expression,it is 
#  immediately replaced with the object that it currently refers to,
#  whatever that may be. Further, all variables must be explicitly 
#  assigned before they can be used; referencing unassigned variables
#  results in errors

a = 3

#1 Create an object to represent the value 3
#2 Create the variable a, if it does not yet exist
#3 Link the variable a to the new object 3

#Objects

#Objects are pieces of allocated memory, with enough space to represent
#the values for which they stand and two standard header fileds:a type
#designator used to mark the type of the object(a poniter to an object 
#called int, the name of the integer type etc) and a reference counter
#used to determine when it's OK to reclaim the object which is to say 
#that the object's space is automatically thrown bakc into the free space
#tool, to be reused for a future object.

#References

#References are automatically followed pointers from variables to objects
