# -*- coding: utf-8 -*-
"""
Created on Tue May 17 07:01:02 2022

@author: Reza
"""

from countryinfo import CountryInfo
count = input("Enter your country :")
country = CountryInfo(count)
print("Capital is : ",country.capital())
print("Currencies is : ",country.currencies())
print("language is : ", country.languages())
print("Borders are : ",country.borders())
print("Others names : ", country.alt_spelling())
