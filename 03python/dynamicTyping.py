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


#Shared References and immutable objects
a = 3
print( id(a) )
b = a 
print( id(b) )
a = 'spam'
print( id(a) )
b = b + 2
print( id(b) )

#Shared References and mutable objects
import copy
#List
L1 = [2]
temp = [1]
L1.append(temp)
L2 = L1 # not copy
L3 = L1[:] # top-level shallow copy
L4 = list(L1) # top-level shallow copy
#L5 = L1.copy() # top-level shallow copy and only for Python 3.3 and later
L6 = copy.copy(L1) # top-level shallow copy
L7 = copy.deepcopy(L1) # deep copy
#result =( L1,L2,L3,L4,L5,L6,L7 )
result =( L1,L2,L3,L4,L6,L7 )
print( result )
temp[0] = 3
print( result )

#dict
d1 = {'a':1}
d2 = d1 # not copy
d3 = d1.copy() #top-level shallow copy
d4 = dict( d1 ) #top-level shallow copy
d5 = copy.copy( d1 ) #top-level shallow copy
d6 = copy.deepcopy( d1 ) #deep copy

#set
s1 = {1}
s2 = s1 # not copy
s3 = s1.copy() #top-level shallow copy
s4 = set( s1 ) #top-level shallow copy
s5 = copy.copy( s1 ) #top-level shallow copy
s6 = copy.deepcopy( s1 ) #deep copy

#the getrefcount function in the standard sys module returns the object's
#reference count
import sys
print( sys.getrefcount(1) )
