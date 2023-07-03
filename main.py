# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 02:29:49 2022

@author: Kush Bhandari
"""

#RQ1
class Cheer:
    def func1(self, s):
        self.s = s
        self.index = -1

    def func2(self):
        return Cheer(self.s)

    def func3(self):
        self.index += 1
        if self.index == len(self.s):
            raise StopIteration
        return "Give me an: " + self.s[self.index]


#RQ2
class Countdown:
    
    def func1(self, num):
        self.count = num

    def func2(self):
        return Countdown(self.count)

    def func3(self):
        if self.count < 0:
            raise StopIteration
        n = self.count
        self.count -= 1
        return n


##############
# Generators #
##############

def naturals():
    
    temp = 1
    while True:
        yield temp
        temp += 1
# RQ3
def evens():

    temp1 = 2
    while True:
        yield temp1
        temp1 += 2

#RQ4
def scale(s, k):

    yield from map(lambda x: x * k, s)

# RQ5
def countdown(n):

    temp2 = n
    while temp2 >= 0:
        yield temp2 
        


# RQ6
def hailstone(n):

    temp3 = n
    while temp3 >=1:
        if temp3 ==1:
            yield 1
            return 1
        if temp3 %2==0:
            yield temp3 
            temp3 =temp3//2
        else:
            yield temp3 
            temp3 = 3*temp3 +1
