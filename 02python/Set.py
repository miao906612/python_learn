# -*- coding: utf-8 -*-
#########################################################################
# File Name: Set.py
# Author: Shuo Miao
# mail: miao906612@163.com
# Created Time: 2015年11月23日 10:31:38
#########################################################################

#Set basics in Python 2.6 and earlier

#make a set
#pass in a sequence or other iterable object to the built-in set function
x = set( 'abcde' )
print( x )
y = set( 'bdxyz' )
print( y )
temp = set( ['a', 'b', 'c', 'd', 'e'])
print( temp )
temp = set( ('a', 'b', 'c') )
print( temp )
temp = { 1, 2, 3, 4}
print( temp )
temp = set() #the only way to get an empty set
print( temp )

#mathematical set operations with expression operators
#Note that we cannot perform the following operations on plain sequences
#like strings,lists and tuples
print( x - y ) #difference
print( x | y ) #union
print( x & y ) #intersection
print( x ^ y ) #symmetric difference
print( x > y ) #test if x is a superset of y
print( x < y ) #test if x is a subset of y

#in membership test
#this expression is also defined to work on all other collection types
print( 'e' in x )
print( 'e' in 'Camelot' )
print( 22 in [11, 22, 33] )

#Iterable containers
#As iterable containers, sets can also be used in operations such as len,
#for loops, and list comprehensions. Because they are unsorted, they don't
#support sequence operations like indexing and slicing
for item in set( 'abdcd' ):
	print( item * 3 )

#Set object provides methods that correspond to the expression operators
#and more, and the support set changes.
z = x.intersection(y)
print( z )
z.add('SPAM') #insert one item
print( z )
z.update( set(['X','Y']) ) #Merge:in-place union
print( z )
z.remove( 'b' ) #delete one item
print( z )
#set expressions shown earlier generally require two sets, their
#method-based counterparts can often work with any iterable type as well
S = set( [1,2,3] )
S | set([3,4])
#S | [3,4]
print( S.union([3,4]) )
print( S.intersection( (1,3,5) ) )
print( S.issubset( range(-5,5) ) )

#Immutable constraints
#Sets can only contain immutable object types. Hence, lists and 
#dictionaries cannot be embedded in sets, but tuples can if you need to 
#store compound values. Tuples compare by their full values when used in
#set operations
S = set()
S.add(1.23)
#S.add([1,2,3])
#S.add({'a':1})
#S.add( set([1,2,3]) )
S.add( (1,2,3) )
print( S )
S.add( (1,4,5) )
print( S )
S.update( {(1,2,3),(4,5,6),(7,8,9)} )
print( S )
print( (1,2,3) in S )
print( (7,8,9) in S )
print( ('1','b','c') in S )








