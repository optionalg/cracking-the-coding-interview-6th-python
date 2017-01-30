"""
1.2 - Check Permutation: Given two strings, write a method to decide if one is a permutation of the other
"""

def checkPermutation(str1, str2):
    if len(str1) != len(str2):
        return False
    keys = {}
    for s in str1:
        keys[s] = keys.get(s,0) + 1
    for s in str2:
        if keys[s] == 0:
            return False
        keys[s] = keys.get(s) - 1
    return True

key_1 = "abcdefeef"
key_2 = "feeeedcba"
print(key_1,key_2,checkPermutation(key_1,key_2))
