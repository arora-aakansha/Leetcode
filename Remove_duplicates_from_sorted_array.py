#problem statement
'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such 
that each unique element appears only once. The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums 
initially. The remaining elements of nums are not important as well as the size of nums.
Return k

'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #if list is empty return 0
        if len(nums)==0:
            return 0
        index = 0 #initialize the index
        for i in range(1, len(nums)):
            if nums[i] != nums[index]: #compare with previous 
                index +=1
                nums[index]=nums[i]
        return index+1
                
            
        