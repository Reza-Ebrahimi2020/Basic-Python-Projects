# -*- coding: utf-8 -*-
"""
Created on Tue May 17 13:10:21 2022

@author: Reza
"""

def least_common_multiple(a,b):
    
    if a > b :
        greater = a
    elif b > a:
        greater = b
        while(True):
            if((greater % a==0) and (greater % b == 0)):
                lcm = greater
                break
            greater = greater + 1
        return lcm
    
a=int(input("Enter 1st number: "))
b=int(input("Enter 2st number: "))
print(least_common_multiple(a, b))