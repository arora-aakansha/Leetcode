'''
Problem Statement

Given an integer n, return the number of prime numbers that are strictly less than n.

 

Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 106
   Hide Hint #1  
Checking all the integers in the range [1, n - 1] is not efficient. Think about a better approach.
   Hide Hint #2  
Since most of the numbers are not primes, we need a fast approach to exclude the non-prime integers.
   Hide Hint #3  
Use Sieve of Eratosthenes.
'''

from math import isqrt
class Solution:
    def countPrimes(self, n: int) -> int:
        if n<=2:
            return 0
        prime=[True]*n
        prime[0] = False
        prime[1] = False
        
        for i in range(2,isqrt(n)+1):
            if prime[i]:
                for x in range(i*i,n,i):
                    prime[x]=False
        
        count = 0
        for i in range(len(prime)):
            if prime[i]:
                count+=1
        return count
        