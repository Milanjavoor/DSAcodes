# Daily DSA Practice

A collection of Data Structures and Algorithms problems I'm solving daily to strengthen my coding skills.

## Problems Solved

### 1. Move Zeros
**Problem:** Move all zeros in an array to the end while maintaining the relative order of non-zero elements.

**Approach:** Two-pointer technique
- Use pointer `i` to track position for next non-zero element
- Iterate with pointer `j` to find non-zero elements
- Place non-zero elements at position `i`, then fill remaining positions with zeros

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

```python
def moveZeroes(self, nums):
    n = len(nums)
    i = 0
    for j in range(n):
        if nums[j] != 0:
            nums[i] = nums[j]
            i += 1
    for m in range(i, n):
        nums[m] = 0
```

---

### 2. Maximum Consecutive Ones
**Problem:** Find the maximum number of consecutive 1s in an array.

**Approach:** Linear traversal with counter
- Maintain a counter `k` for current consecutive ones
- Reset counter when encountering 0
- Track maximum count in `maxk`

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

```python
def findMaxConsecutiveOnes(self, nums):
    k = 0
    maxk = 0
    for i in nums:
        if i:
            k += 1
        else:
            if k > maxk:
                maxk = k
            k = 0
    if k > maxk:
        maxk = k
    return maxk
```

---

### 3. Maximum Subarray
**Problem:** Find the subarray with the largest sum and return its sum.

**Approach:** Kadane's Algorithm (Optimized)
- Maintain running sum `total`
- Reset to 0 when sum becomes negative
- Track maximum sum encountered

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

```python
def maxSubArray(self, nums):
    maxi = float('-inf')
    total = 0
    for i in range(len(nums)):
        total += nums[i]
        maxi = max(total, maxi)
        if total < 0:
            total = 0
    return maxi
```

---

### 4. Best Time to Buy and Sell Stock
**Problem:** Find maximum profit from buying and selling stock once.

**Approach:** Single pass with min tracking
- Track minimum price seen so far (`minval`)
- Calculate profit at each price point
- Update maximum profit (`maxprof`)

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

```python
def maxProfit(self, prices):
    n = len(prices)
    maxprof = 0
    minval = float("inf")
    for i in range(n):
        if minval < prices[i]:
            prof = prices[i] - minval
            maxprof = max(maxprof, prof)
        if prices[i] < minval:
            minval = prices[i]
    return maxprof

## Learning Goals

- Master array manipulation techniques
- Understand two-pointer and sliding window patterns
- Learn Kadane's Algorithm for subarray problems
- Build consistent daily coding practice

## Technologies Used

- Language: Python
- Platform: LeetCode

---

*Started: [Add start date]*  
*Location: Hubballi, Karnataka, India*
