"""
Problem: Two Sum (LeetCode #1)
Link: https://leetcode.com/problems/two-sum/
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for a,b in enumerate(nums):
            answer=target-b
            if answer in nums:
                c=nums.index(answer)
                if a!=c:
                    return [a,c]

# Test run
if __name__ == "__main__":
    sol = Solution()
    result = sol.twoSum([2, 7, 11, 15], 9)
    print(result)  # Output: [0, 1]