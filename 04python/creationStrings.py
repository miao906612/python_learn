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

#Escape Sequences
#Note that the origin backslash characters are not really stored with the 
#string in memory; they are used only to describe special character values
#to be stored in the string. For coding such special characters, Python
#recognizes a full set of escape code sequences, listed as below

# \\			Backslash(stores one \)
# \'			Single quote(stores ')
# \"			Double quote(stores ")
# \a			Bell
# \b			Backspace
# \f			Formfeed
# \n			Newline(linefeed)
# \r			Carriage return
# \t			Horizontal tab
# \v			Vertical tab
# \xhh			Character with hex value hh(exactly 2 digits)
# \ooo			Character with octal value ooo(up to 3 digits)
# \0			Null:binary 0 character(doesn't end string)
# \N{ id }		Unicode database ID
# \uhhhh		Unicode character with 16-bit hex value
# \Uhhhhhhhh	Unicode character with 32-bit hex value
# \other		Not an escape(keeps both \ and other)


# Raw Strings Suppress Escapes

# For example
myfile=open("C:\new\tata",w);
# This one is translated into "C:(newline)ew(tab)ata" which is not wanted
myfile=open(r"C:\new\tata")
myfile=open("C:\\new\\tata")
# we can use forward slashes in directory paths on windows and Linux
myfile=open("C:/new/tata")


# Triple Quotes Code Multiline Block Strings
# Triple quotes """ """ is a syntactic convenience for coding multiline 
# text data.
mantra = """Always look
    on the bright
    side of life."""
# Note that if we want to print what we enter just as the way it is,
# print() function should be used instead of echoing mechanism
print(mantra)

# Note that the trible quotes will retain all the enclosed text, 
# including any to the right of your code that might intend as comments
menu = """spam      # comments have add to string
    eggs            # ditta
    """
# Trible quotes is used where multiline text is needed such as multiline
# error messages, HTML, XML or JSON code.

# Trible quotes are also commonly used for documentation strings, which 
# are string literals that are taken as comments when they appear at 
# specific points in your file
def add(int a, int b):
    """ this function is used to add two integers """
    return a + b

# Trible quotes are sometimes used to comment lines of your code
# during development
X = 1
"""
import os
print(os.getcwd())
"""
Y = 2
































