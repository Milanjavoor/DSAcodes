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
