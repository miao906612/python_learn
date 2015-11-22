# -*- coding: utf-8 -*-
#########################################################################
# File Name: Fraction.py
# Author: Shuo Miao
# mail: miao906612@163.com
# Created Time: 2015年11月22日 17:56:15
#########################################################################

#Fraction basics
from fractions import Fraction
x = Fraction(1,3)
y = Fraction(4,6)
print(x)
print( y )
print( x + y )
print( x - y )
print( x * y )
temp = Fraction('.25')
print( temp )
temp = Fraction( '1.25' )
print( temp )
temp = Fraction( '.25' ) + Fraction( '1.25' )
print( temp )
temp = Fraction( 1.25 ) #2.7 and 3.4 but not 2.6
print( temp )

#Numeric accuracy in fractoins and decimals
temp = 0.1 + 0.1 + 0.1 - 0.3
print( temp )
from fractions import Fraction
temp = Fraction(1,10) + Fraction(1,10) + Fraction(1,10) - Fraction(3,10)
print( temp )
from decimal import Decimal
temp = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
print( temp )

#Fraction conversions and mixed types

#floating-point number to Fraction
temp = Fraction.from_float(1.75)
print( temp )
temp = Fraction( 1.75 )
print( temp )
temp = Fraction( *(1.75).as_integer_ratio() )
print( temp )
#Fraction to floating-point numbers
temp = float( x )
print( temp )
#type mixing in expressions
temp = x + 2 #Fraction + int -> Fraction
print( temp )
temp = x + 2.0 #Fraction + float -> float
print( temp )
