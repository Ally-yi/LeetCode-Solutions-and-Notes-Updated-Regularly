"""
Problem: Top K Frequent Elements (LeetCode #347)
Link: https://leetcode.com/problems/top-k-frequent-elements/
"""

from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        counts = Counter(nums)

        sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)

        result = [item[0] for item in sorted_counts[:k]]

        return result


solution = Solution()
nums1 = [1, 1, 1, 2, 2, 3]
k1 = 2
print(f"Input: nums = {nums1}, k = {k1}")
print(f"Output: {solution.topKFrequent(nums1, k1)}")  

nums2 = [1]
k2 = 1
print(f"Input: nums = {nums2}, k = {k2}")
print(f"Outpu: {solution.topKFrequent(nums2, k2)}") 