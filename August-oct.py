46. Permutations
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        final=[]
        if len(nums)==0:
            return [[]]
        perms=self.permute(nums[1:])
        for p in perms:
            for i in range(n+1):
                p_copy=p.copy()
                p_copy.insert(i,nums[0])
                if p_copy not in final:
                    final.append(p_copy)
        return final
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final=[]
        new=[]
        visited={num:False for num in nums}
        def solve():
            if len(nums)==len(new):
                final.append(new[:])
                return
            for num in nums:
                if visited[num]==True:
                    continue
                new.append(num)
                visited[num]=True
                solve()
                new.pop()
                visited[num]=False
        solve()
        return final
1464. Maximum Product of Two Elements in an Array

Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1)
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        return ((nums[n-1]-1)*(nums[n-2]-1))
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n=len(nums)
        return ((nums[n-1]-1)*(nums[n-2]-1))
 4. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        new=nums1+nums2
        new.sort()
        n=len(new)
        if n%2==0:
            med= (new[(int(n/2))]+new[(int((n/2)-1))])/2
        else:
            med= new[n//2]
        return(med)
134. Gas Station
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
