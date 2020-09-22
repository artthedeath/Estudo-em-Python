# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 12:52:41 2020

@author: arthu
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def set_width(self,width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2)** 0.5
    
    def get_picture(self):
        x = 0
        d=''
        if self.width >50 or self.height > 50:
            return 'Too big for picture.'
        else:
            while x < self.height:
                d += '*' * self.width + '\n'
                x += 1
            return d
    
    def get_amount_inside(self,arg):
        return self.get_area()//arg.get_area()



class Square(Rectangle):
    def __init__(self,side, width = 0, height = 0):
        self.side = side
        self.set_height(side)
        self.set_width(side)
        
    def __str__(self):
        return f'Square(side={self.width})'
    
    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side
    
    def set_height(self,side):
        self.height = side
        
    def set_width(self,side):
        self.width = side
        
        
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())
 
sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())
 
rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
 