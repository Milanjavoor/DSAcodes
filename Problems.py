class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=0
        for j in range(n):
            if nums[j]!=0:
                nums[i]=nums[j]
                i=i+1
        for m in range(i,n):
            nums[m]=0
#problem 2 : problem 485 Maximum consecutive ones
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=0
        maxk=0
        for i in nums:
            if i:
                k=k+1
            else:
                if k>maxk:
                    maxk=k
                k=0
        if k>maxk:
            maxk=k
        return maxk
        
        return max(maxk,k)
 # problem 3 . Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.       
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi=float('-inf')
        for i in range(0,len(nums)):
            total=0
            for j in range(i,len(nums)):
                total=total+nums[j]
                maxi= max(total,maxi)
        return maxi
