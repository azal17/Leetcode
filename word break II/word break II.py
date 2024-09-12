from os import *
from sys import *
from collections import *
from math import *

def wordBreak(s, dictionary):
    word_set = set(dictionary)

    memo = {}

    def backtrack(start):
        if start in memo:
            return memo[start]
        
        result = []

        if start == len(s):
            return[""]

        for end in range(start+1, len(s)+ 1):
            word = s[start:end]
            if word in word_set:
                remaining_sentences = backtrack(end)
                for sentence in remaining_sentences:
                    if sentence:
                        result.append(word + " " + sentence)
                    else:
                            result.append(word)
        memo[start] = result
        return result
    return backtrack(0)
            


    
