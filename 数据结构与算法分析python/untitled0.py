# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 21:24:22 2023

@author: 23665
"""

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    quene=[]
    length=0
    for string in s:
        if string in quene:
            length=max(length,len(quene))
            #如果在列表中，那么就删除列表中的元素，知道不在列表中，
            #也就是从新的元素开始计算
            while string in queue:
                quene.pop(0)
        quene.append(string)
    return max(length,len(quene))
print(lengthOfLongestSubstring("abcabcbb"))