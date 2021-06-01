# -*- coding: utf-8 -*-
"""
Created on Fri May 28 13:31:56 2021

@author: Mac_1
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import turtle as t
for i in range(3):
    t.forward(100)
    t.left(360/3)
    
    t.penup()
    t.forward(200)
    t.pendown()
    
    for i in range(4):
        t.forward(100)
        t.left(360/4)
        
        t.done()