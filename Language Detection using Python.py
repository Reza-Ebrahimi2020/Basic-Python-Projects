# -*- coding: utf-8 -*-
"""
Created on Tue May 17 15:34:22 2022

@author: Reza
"""

from langdetect import detect
text = input("Enter any text in any language:")
print(detect(text))

