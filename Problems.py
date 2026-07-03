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
class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        ans=[0]*n
        pos=0
        neg=1
        for i in nums:
            if i>0:
                ans[pos]=i
                pos+=2
            else:
                ans[neg]=i
                neg+=2
        return ans

54. Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n=len(matrix)
        m=len(matrix[0])
        top=0
        bot=n-1
        right=m-1
        left=0
        result=[]
        while top<=bot and left<=right:
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top+=1
            for i in range(top,bot+1):
                result.append(matrix[i][right])
            right-=1
            if top<=bot:
                for i in range(right,left-1,-1):
                    result.append(matrix[bot][i])
                bot-=1
            if left<=right:
                for i in range(bot,top-1,-1):
                    result.append(matrix[i][left])
                left+=1
        return result

18. 4Sum

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == targe
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    for m in range(k+1,len(nums)):
                        s=nums[i]+nums[j]+nums[k]+nums[m]
                        o=[nums[i],nums[j],nums[k],nums[m]]
                        if s==target:
                            if o not in result:
                                result.append(o)
                            else:
                                pass
                        else:
                            pass
        return result
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                myset=set()
                for l in range(j+1,len(nums)):
                    k=target-(nums[i]+nums[j]+nums[l])
                    if k in myset:
                        new=[nums[i],nums[j],nums[l],k]
                        new.sort()
                        if new not in result:
                            result.append(new)
                    myset.add(nums[l])
        return result
       
