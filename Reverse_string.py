#problem
'''
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length =len(s)
        for i in range(length//2):
            s[i], s[length-1-i] = s[length-1-i], s[i]
        return s
        