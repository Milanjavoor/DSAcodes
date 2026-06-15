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
 n=len(nums)
        total=0
        maxi=float("-inf")
        for i in range(0,n):
            total=total+nums[i]
            maxi=max(total,maxi)
            if total<0:
                total=0
        return maxi
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num,res=0,0
        max=nums[0]
        for i in nums:
            if res<0:
                res=i
            else:
                res+=i
            if max<res:
                max=res
        return max
        121. Best Time to Buy and Sell Stock
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        maxprof=0
        minval=float("inf")
        for i in range(0,n):
            if minval<prices[i]:
                prof=prices[i]-minval
                maxprof=max(maxprof,prof)

            if prices[i]<minval:
                minval=prices[i]
        return maxprof
    #15. 3Sum
    class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                if s>0:
                    r-=1
                elif s<0:
                    l+=1
                else:
                    result.append((nums[i],nums[l],nums[r]))
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    r-=1
                    l+=1
                 
        return result


#2149. Rearrange Array Elements by Sign
class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        pos=[]
        neg=[]
        for i in range(n):
            if nums[i]<0:
                neg.append(nums[i])
            else:
                pos.append(nums[i])
        for i in range(0,n):
            if i==1:
                nums[i]=(neg[0])
            else:
                if i%2==0:
                    nums[i]=pos[i//2]
                else:
                    nums[i]=neg[i//2]
        return nums
