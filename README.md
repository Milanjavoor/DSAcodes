Daily DSA Practice

A collection of Data Structures and Algorithms problems I'm solving daily to strengthen my problem-solving skills and prepare for coding interviews. The repository focuses on mastering common array techniques, two-pointer methods, greedy algorithms, and optimized searching strategies.

Problems Solved
1. Move Zeroes

Problem: Move all zeros in an array to the end while maintaining the relative order of non-zero elements.

Approach: Two Pointer Technique
Maintain pointer i for the next position of a non-zero element.
Traverse the array using pointer j.
Place every non-zero element at index i.
Fill the remaining positions with zeros.

Time Complexity: O(n)

Space Complexity: O(1)

2. Maximum Consecutive Ones

Problem: Find the maximum number of consecutive 1s in a binary array.

Approach: Linear Traversal
Maintain a counter for current consecutive ones.
Reset the counter whenever 0 is encountered.
Track the maximum streak.

Time Complexity: O(n)

Space Complexity: O(1)

3. Maximum Subarray

Problem: Find the contiguous subarray having the largest sum.

Approach: Kadane's Algorithm
Maintain a running sum.
Reset the running sum whenever it becomes negative.
Track the maximum sum throughout the traversal.

Time Complexity: O(n)

Space Complexity: O(1)

4. Best Time to Buy and Sell Stock

Problem: Find the maximum profit that can be achieved from buying and selling a stock once.

Approach: Greedy
Keep track of the minimum stock price seen so far.
Compute the profit for each day.
Update the maximum profit whenever a larger profit is found.

Time Complexity: O(n)

Space Complexity: O(1)

5. 3Sum

Problem: Find all unique triplets whose sum equals zero.

Approach: Sorting + Two Pointers
Sort the array.
Fix one element.
Use two pointers to search for the remaining two numbers.
Skip duplicate values to avoid repeated triplets.

Time Complexity: O(n²)

Space Complexity: O(1) (excluding output)

6. Rearrange Array Elements by Sign

Problem: Rearrange an array so that positive and negative numbers alternate while maintaining their relative order.

Approach 1: Extra Positive & Negative Arrays
Store positive and negative numbers separately.
Place them alternately into the original array.

Time Complexity: O(n)

Space Complexity: O(n)

Approach 2: Optimized Auxiliary Array
Create an answer array.
Maintain two indices:
pos = 0
neg = 1
Place positive numbers at even indices and negative numbers at odd indices.

Time Complexity: O(n)

Space Complexity: O(n)

7. Spiral Matrix

Problem: Return all elements of a matrix in spiral order.

Approach: Boundary Traversal

Maintain four boundaries:

Top
Bottom
Left
Right

Traverse each boundary one by one while shrinking the boundaries after every traversal.

Time Complexity: O(m × n)

Space Complexity: O(1) (excluding output)

8. 4Sum

Problem: Find all unique quadruplets whose sum equals the target.

Approaches Implemented
Brute Force
Check every possible quadruplet.
Store unique answers.

Time Complexity: O(n⁴)

Space Complexity: O(1)

Better Approach (Hash Set)
Fix two numbers.
Use a hash set to find the remaining pair.
Remove duplicates before storing.

Time Complexity: O(n³)

Space Complexity: O(n)

Optimal Approach (Sorting + Two Pointers)
Sort the array.
Fix the first two numbers.
Use two pointers to find the remaining pair.
Skip duplicate values for uniqueness.

Time Complexity: O(n³)

Space Complexity: O(1) (excluding output)

Patterns Covered
Two Pointer Technique
Greedy Algorithms
Kadane's Algorithm
Array Traversal
Sorting
Hashing
Two Pointer after Sorting
Boundary Traversal
Duplicate Elimination
In-place Array Manipulation
Learning Goals
Strengthen array manipulation techniques.
Master the two-pointer pattern.
Learn greedy optimization strategies.
Understand Kadane's Algorithm.
Practice hash-based searching.
Solve interview-standard problems with multiple approaches.
Improve time and space complexity optimization skills.
Technologies Used
Language: Python
Platform: LeetCode
Concepts: Arrays, Greedy, Hashing, Sorting, Two Pointers, Dynamic Programming Basics
Complexity Summary
Problem	Best Time	Space
Move Zeroes	O(n)	O(1)
Maximum Consecutive Ones	O(n)	O(1)
Maximum Subarray	O(n)	O(1)
Best Time to Buy & Sell Stock	O(n)	O(1)
3Sum	O(n²)	O(1)
Rearrange Array by Sign	O(n)	O(n)
Spiral Matrix	O(m × n)	O(1)
4Sum	O(n³)	O(1)
Repository Highlights
✔️ Multiple approaches for the same problem (Brute Force → Better → Optimal).
✔️ Clean and beginner-friendly Python implementations.
✔️ Covers several popular interview patterns.
✔️ Focuses on writing optimized solutions after understanding brute-force approaches.
✔️ Designed as a daily DSA practice repository for continuous improvement.


Remove Duplicates from Sorted Array
A Python solution to remove duplicate elements from a sorted integer array in-place. The algorithm uses a two-pointer approach to modify the array efficiently without allocating extra space for another array.

🚀 How It Works
The function uses two pointers to process the array:

i (the scanner): Iterates through the array from left to right.

l (the writer): Tracks the index where the next unique element should be placed
