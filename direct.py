# -*- coding: utf-8 -*-
"""
Created on Fri May 21 14:40:05 2021

@author: Mac_1
"""

import turtle as t

t.width(3)
t.shape("turtle")
t.shapesize(3, 3)

while True:
      comand = t.textinput("방향 결정", "l이나 r 입력")
      if comand == "L":
         t.left(90)
         t.forward(100)
      if comand == "r":
         t.right(90)
         t.foward(100)