"""
Problem: Contains Duplicate(LeetCode #217)
Link: https://leetcode.com/problems/contains-duplicate/
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))

# ---------- Test ----------
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [1, 2, 3, 4],         # No duplicates
        [1, 2, 3, 1],         # Duplicate 1
        [1],                  # Single element
        [1, 1, 1, 1],         # All duplicates
        [0, -1, -2, -1],      # Duplicate negative number
        [],                  # Empty list
        [10, 20, 30, 40, 10], # Duplicate 10
    ]

    for nums in test_cases:
        result = solution.containsDuplicate(nums)
        print(result)