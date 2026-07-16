# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
a = [1, 2, 3, 3]
b=list(set(a))

if a != b:
    print('true')
else:
    print('false')

nums = [1, 2, 3, 4]
nums2 =list(set(nums))

if nums != nums2:
    print('true')
else:
    print('false')

# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
s = "racecar"
t = "carrace"

s1='jar'
t1='jam'

if sorted(s1) == sorted(t1):
    print('true')
else:
    print('false')
 