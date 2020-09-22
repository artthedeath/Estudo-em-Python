# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 16:15:56 2020

@author: Arthur DOnizeti Rodrigues Dias
"""
from copy import deepcopy
import random

class Hat:
    def __init__(self, **balls):
        self.balls = balls 
        self.lista_cor =[]
        self.lista_remove=[]
        self.contents = self.contents()
        
    def contents(self):
        for k,v in self.balls.items():
            n = v
            while n > 0:
                self.lista_cor.append(k)
                n -=1
        return self.lista_cor
    def draw(self,num):
        if num >len(self.lista_cor):
            self.lista_remove = self.lista_cor.copy()
        else:
            while num > 0:
                x = random.choice(self.lista_cor)
                self.lista_remove.append(x)
                self.lista_cor.remove(x)
                num -= 1
        return self.lista_remove
        


def experiment(hat,expected_balls, num_balls_drawn, num_experiments):
    m = 0
    n = num_experiments
    
    while n > 0:
        
        x = deepcopy(hat)
        x.contents
        y = {}
        
        for cor in x.draw(num_balls_drawn):
            y.setdefault(cor,0)
            y[cor] = y[cor]+1
        aux = 0
        for keys2 in y.keys():
            for keys in expected_balls.keys():
                if keys == keys2:
                    if y[keys] >= expected_balls[keys]:
                        aux += 1
        if aux == len(expected_balls):
            m += 1
        n -= 1
        
    return float(m)/float(num_experiments)


