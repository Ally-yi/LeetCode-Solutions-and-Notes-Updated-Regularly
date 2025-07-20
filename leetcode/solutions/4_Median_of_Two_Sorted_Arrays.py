"""
Problem: Median of Two Sorted Arrays (LeetCode #4)
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = []       # Merged sorted array
        i = j = 0

        # Merge two sorted arrays
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                a.append(nums1[i])
                i += 1
            else:
                a.append(nums2[j])
                j += 1

        # Append any remaining elements
        while i < len(nums1):
            a.append(nums1[i])
            i += 1
        while j < len(nums2):
            a.append(nums2[j])
            j += 1

        # Calculate median
        n = len(a)
        if n % 2 == 0:
            mid = n // 2
            return (a[mid - 1] + a[mid]) / 2
        else:
            mid = n // 2
            return a[mid]

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(result)
