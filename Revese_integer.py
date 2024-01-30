'''
Problem Statement 

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1

'''

#Solution -1

class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -(2**31)
        INT_MAX = 2**31
        
        x_string = str(x)
        
        rev_str = x_string[::-1]
        if rev_str[-1] == '-':
            rev_str = "-" + rev_str[:-1]
        if int(rev_str) not in range(INT_MIN, INT_MAX):
            return 0
        return int(rev_str)
    
    
#Solution -2 
class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -(2**31)
        INT_MAX = 2**31
        if x == 0:
            return 0
        s=''
        if x<0:
            x=-x
            s+="-"
        while x:
            rem = x%10
            s += str(rem)
            x=x//10
        if int(s) not in range(INT_MIN, INT_MAX):
            return 0
        return int(s)
