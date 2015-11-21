import random
temp = dir( random )
for content in temp:
	tempData = content.find( '_' )
	if( tempData != 0 ):
		print( content )
