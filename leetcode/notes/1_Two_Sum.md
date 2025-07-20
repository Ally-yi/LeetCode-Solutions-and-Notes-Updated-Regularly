# Two Sum (LeetCode #1)

**Problem Link:** [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/)

---

## Problem Description

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.  
You may assume that each input would have **exactly one solution**, and you may not use the same element twice.  

## Key Python Method: `enumerate( )`

- `enumerate()` is a built-in Python function that allows you to loop over an iterable (like a list) and have an automatic counter.
- It returns pairs of `(index, value)` for each element in the iterable.
- Example

  ```python
  for index, value in enumerate(['a', 'b', 'c']):
      print(index, value)
    ```
    output：
    ```python
    0 a
    1 b
    2 c
    ```

## Solution Approach

- Iterate through each number `b` in the list `nums` with its index `a`.
- For each number, calculate the complement `answer = target - b`.
- Check if `answer` exists in the list `nums`.
- If yes, get the index `c` of `answer`.
- If `a` and `c` are different indices, return `[a, c]` as the solution.

This approach uses a brute-force search by checking membership and index lookup in the list.


## Code

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for a,b in enumerate(nums):
            answer = target - b
            if answer in nums:
                c = nums.index(answer)
                if a != c:
                    return [a, c]

# Test run
if __name__ == "__main__":
    sol = Solution()
    result = sol.twoSum([2, 7, 11, 15], 9)
    print(result)  # Output: [0, 1]
