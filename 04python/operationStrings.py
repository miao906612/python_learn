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
