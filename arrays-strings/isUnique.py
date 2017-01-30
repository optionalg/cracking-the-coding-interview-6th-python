"""
1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters.
 What if you cannot use additional data structures
"""

def isUnique(chars):
    if len(chars) > 128:
        return False
    char_set = [False for _ in range(128)]
    for c in chars:
        value = ord(c)
        if char_set[value]:
            return False
        char_set[value] = True
    return True

unique = "abcdefghkilmnopqrstuvwx"

print("The String",unique," is ",isUnique(unique))
