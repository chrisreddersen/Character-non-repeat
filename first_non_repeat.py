# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 07:22:01 2019

@author: creddersen
"""

def first_non_repeating_letter(string):
        list = [i.lower() for i in string]
        for i in range(len(list)):
            if list.count(list[i]) == 1:
                return string[i]
            return ""
        
        
    