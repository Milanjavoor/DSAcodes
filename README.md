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
# 4Sum - LeetCode (Python)

## Problem Statement

Given an array `nums` of `n` integers, return all unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:

- `0 <= a, b, c, d < n`
- `a`, `b`, `c`, and `d` are distinct.
- `nums[a] + nums[b] + nums[c] + nums[d] == target`

The solution should not contain duplicate quadruplets.

---

## Approach

This solution uses:

- Sorting the input array.
- Two nested loops to fix the first two elements.
- A two-pointer technique to efficiently find the remaining two elements.
- Duplicate skipping to ensure only unique quadruplets are returned.

This approach significantly reduces unnecessary computations compared to checking every possible combination.

---

## Algorithm

1. Sort the array.
2. Iterate through the array with the first pointer.
3. Use a second loop for the second pointer.
4. Initialize two pointers (`left` and `right`) for the remaining elements.
5. Compare the current sum with the target:
   - If equal, store the quadruplet.
   - If smaller, move the left pointer.
   - If larger, move the right pointer.
6. Skip duplicate values at every stage.
7. Return the list of unique quadruplets.

---

## Time Complexity

- **Sorting:** `O(n log n)`
- **Nested loops + Two pointers:** `O(n³)`

**Overall:** `O(n³)`

---

## Space Complexity

- **Auxiliary Space:** `O(1)` (excluding the output list)
- **Output Space:** Depends on the number of valid quadruplets.

---

## Features

- Efficient `O(n³)` solution.
- Avoids duplicate quadruplets.
- Uses the two-pointer technique after sorting.
- Clean and optimized Python implementation.

