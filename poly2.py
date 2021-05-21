# -*- coding: utf-8 -*-
"""
Created on Fri May 21 15:32:50 2021

@author: Mac_1
"""

import turtle as t
t.shape("turtle")
s = turtle.textinput("", "도형을 입력하시오: ")
if s == "사각형" :
   s = turtle.textinput(""."가로: ")
   w=int(s)
   s = turtle.textinput(""."세로: ")
   h=int(s)
   t.fonward(w)
   t.left(90)
   t.forward(h)
   t.left(90)
   t.forward(w)
   t.left(90)
   t.forward(h)
elif s == "삼각형":   
    