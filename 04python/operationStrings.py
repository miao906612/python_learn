# -*- coding: utf-8 -*-
# Copyright 2016 Baidu Inc. All Rights Reserved.
# Author: Shuo Miao (miaoshuo@baidu.com)
#

# Basic operations
len("abc")              # Length:number of items
"abc" + "def"           # Concatenation: a new string
"NI!" * 3               # Repetition: like "NI!" + "NI!" + "NI!"
myjob = "hacker"
for c in myjob:
    # print(c, end=" ") 3.x
    print(c)
"k" in myjob            # In: to determine if "k" is a substring in myjob

# Indexing and Slicing
S = "spam"
print(S)
print(S[0], S[-2])
print(S[1:3], S[1:], S[:-1])
# Extending slicing: The third limit and slice object
S = "abcdefghijklmnop"
print(S[1:10:2])
print(S[::2]) # the default bound is 0 and the length of the sequence
# reverse the strings
print(S[::-1]) # -1 means from right to left

# slicing is equivalent to indexing with a slicing object,
# a finding of importance to class writers seeking to support both
# operations
print("spam"[1:3])
print("spam"[slice(1, 3)])
print("spam"[::-1])
print("spam"[slice(None, None, -1)])

# some common cases used where Slices will be used

# The argument words listed on a system command line used to launch
# a python program are made available in the argv attribute of the 
# built-in sys module
import sys
print(sys.argv)

# To remove the last newline of contents read from a file
line = "This is a text\n"
print(line[:-1])
print(line.rstrip())

