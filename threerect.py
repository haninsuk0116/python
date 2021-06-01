# -*- coding: utf-8 -*-
"""
Created on Fri May 28 14:29:19 2021

@author: Mac_1
"""

import turtle as t
def drawRect(length):
    for i in range(4):
        t.forward(length)
        t.left(90)
        
for i in range(-200,400, 200):
       t.up()
       t.goto(i,0)
       t.down()
       t.drawRect(100)
       
       t.done()
       t.bye()