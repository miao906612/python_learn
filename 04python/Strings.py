# -*- coding: utf-8 -*-
#########################################################################
# File Name: Strings.py
# Author: Shuo Miao
# mail: miao906612@163.com
# Created Time: 2015年11月27日 10:32:35
#########################################################################

#Python address text and binary data differently, with distinct string 
#object types and file interfaces for each.


#In python 3.X there are three string types:

#1 str is used for Unicode text( including ASCII)
#2 bytes is used for binary data( including encoded text )
#3 bytearray is a mutable variant of bytes

#Files work in teo modes:
#1 text represents content as str and implements Unicode encodings
#2 binary deals in raw bytes and does no data translation


#In python 2.X, unicode strings represent Unicode text, str strings handles
#bit text and binary data, and bytearray is available in 2.6 and later as a
#back-port from 3.X
#Normal files' content is simply bytes represented as str, but a codecs
#module opens Unicode text files, handles encodings, and represents content
#as unicode objects

S = 'sp\xc4\u00c4\U000000c4m' #3.x:normal str strings are Unicode text
print( S )
print( type(S) ) #show type. Both 2.X and 3.X are str,but different results
#                are printed
S = '\xc4' #3.x:but this string is ascii text
print( S )
print( type(S) )
S = u'sp\xc4\u00c4\U000000c4m' #The 2.X Unicode literal works in 3.3+:just str
print( S ) #Both 3.X and 2.X gives the same results
print( type(S) ) #3.X shows str type and 2.X shows unicode type
S = b'a\x01c' #3.X:bytes strings are byte-based data
print( S ) #Both can do
print( type(S) ) #3.X shows bytes type and 2.X shows str type


#String literals

#1 single quotes: 'spa"m'
#2 Double quotes: "spa'm"
#3 Triple quotes: '''... spam ... ''', """... spam ..."""
#4 Escape sequences: "s\tp\na\Om"
#5 Raw strings: r"c:\new\test.spm"
#6 Bytes literals in 3.X and 2.6+: b'sp\x01am'
#7 Unicode literals in 2.X and 3.3+: u'eggs\u0020spam'

#single and double quoted strings
S = 'abc',"abc" #the same
print( S )
S = 'ab"c',"ab'c", 'ab\"c',"ac\'c" #embed each other
print( S )
S = "Meaning" 'of' "life" #automatically concatenate adjacent string
print( S )
S = ("Meaning"
		'of'
		'life')
print( S )











































