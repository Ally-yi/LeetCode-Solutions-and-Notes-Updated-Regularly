# Product of Array Except Self (LeetCode \#238)

**Problem Link:** [https://leetcode.com/problems/product-of-array-except-self/](https://leetcode.com/problems/product-of-array-except-self/)
---

## Solution Approach: Two Passes — Left Product and Right Product


#### Step 1: Left Pass

  * Create an array `answer` where `answer[i]` holds the product of **all numbers to the left** of index `i`.
  * For example, in `[1, 2, 3, 4]`, the left products are:
    $[1, 1, 1 * 2, 1 *2 * 3] -> [1, 1, 2, 6]$

#### Step 2: Right Pass

  * Then we go **from right to left**, and multiply each `answer[i]` by the product of all numbers to the **right** of `i`.
  * For the right products:
    $[2 * 3 * 4, 3 * 4, 4, 1] -> [24, 12, 4, 1]$
  * But instead of creating a new array, we keep a running `right` product and multiply it into the existing `answer[i]`.

This works in **O(n)** time, uses only constant extra space (excluding the result array), and **avoids division**.


### Code

```python
"""
Problem: Product of Array Except Self (LeetCode #238)
Link: https://leetcode.com/problems/product-of-array-except-self/
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n 

        left = 1
        for i in range(n):
            answer[i] = left       # current left product
            left *= nums[i]        # update left product

        right = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right     # multiply with right product
            right *= nums[i]       # update right product

        return answer
```

### Why It Works

We build each element `answer[i]` as:

`answer[i]` = (product of all `nums` to the left of `i`) $\\times$ (product of all `nums` to the right of `i`)

By calculating **left product** and **right product** separately, and combining them, we avoid using division and maintain $O(n)$ efficiency.

### Example

**Input:**
`nums = [1, 2, 3, 4]`

**Intermediate steps:**

  * Left products: `[1, 1, 2, 6]`
  * Right products: `[24, 12, 4, 1]`

**Final result** (left * right): `[24, 12, 8, 6]`

**Output:**
`[24, 12, 8, 6]`
