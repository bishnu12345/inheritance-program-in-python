# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:56:51 2019

@author: USER
"""
# Python example to show that base 
# class members can be accessed in 
# derived class using base class name 
class Base():
    def __init__(self, x): 
        self.x = x	 

class Derived(Base): 

	# Constructor 
	def __init__(self, x, y): 
		Base.x = x 
		self.y = y 

	def printXY(self):
        print(self.x, self.y)
        #print(Base.x, self.y) 

# Driver Code 
d = Derived(10,20)
d.printXY()
