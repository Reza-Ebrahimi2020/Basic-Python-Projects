# -*- coding: utf-8 -*-
"""
Created on Tue May 17 16:11:42 2022

@author: Reza
"""

import textwrap

value = """This function wraps the input paragraph such that each
line in the paragraph is at most width characters long. The wrap method
returns a list of output lines. The returned list is empty if the 
wrapped output has no content."""

#wrap this text.
wrapper = textwrap.TextWrapper(width=60)

word_list = wrapper.wrap(text=value)
#print each line.
for element in word_list:
    print(element)