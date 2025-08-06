"""
Problem: Product of Array Except Self(LeetCode #238)
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



if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    solution = Solution()
    result = solution.productExceptSelf(nums)
    print("Input:", nums)
    print("Output:", result)
