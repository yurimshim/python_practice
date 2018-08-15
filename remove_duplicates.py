# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 09:27:24 2018

@author: LG
"""

def remove_duplicates(numbers):
    """
    for every element(numbers[i])in the list, compare with the next one(numbers[i+1])
    append every element(numbers[i]) to result
    but if the element is the same with the next one, do not append it
    """
    result = []
    if len(numbers) <= 1:
        return numbers
    for i in range(len(numbers)):
        if numbers[i] in result:
            continue
        else:
            result.append(numbers[i])
    return result

print(remove_duplicates([1,0,3,29,6,3,4,33,2,2,2,6,83,4,7,5,6,11,1,2]))