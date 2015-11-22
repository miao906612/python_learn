# -*- coding: utf-8 -*-
#########################################################################
# File Name: Decimal_Fraction.py
# Author: Shuo Miao
# mail: miao906612@163.com
# Created Time: 2015年11月22日 17:32:08
#########################################################################

#Decimal basics
print( 0.1+0.1+0.1-0.3)
#######################
from decimal import Decimal
temp = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')
print( temp )
######################
temp = Decimal('0.1') + Decimal('0.1') + Decimal('0.10') - Decimal('0.30')
print( temp )
######################
temp = Decimal(0.1) + Decimal(0.1) +Decimal(0.1) - Decimal(0.3)
print( temp )

#Setting decimal precision globally
import decimal
temp = decimal.Decimal(1) / decimal.Decimal(7)
print( temp )
decimal.getcontext().prec = 4
temp = decimal.Decimal(1) / decimal.Decimal(7)
print( temp )

#Decimal context manager
#In Python 2.6 and 3.0 and later, it's possible to reset the precision
#temporarily by using the with context manager statement
with decimal.localcontext() as ctx:
	ctx.prec = 2
	temp = decimal.Decimal('1.00') / decimal.Decimal('3.00')
	print( temp )
temp = decimal.Decimal('1.00') / decimal.Decimal('3.000')
print( temp )
