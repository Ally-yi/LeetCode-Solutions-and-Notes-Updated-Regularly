"""
Problem: Regular Expression Matching(LeetCode #10)
Link: https://leetcode.com/problems/regular-expression-matching/
"""
import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern = '^' + p + '$'
        return re.match(pattern, s) is not None


if __name__ == "__main__":
    solution = Solution()
    s="mississippi"
    p="mis*is*p*."
    print(solution.isMatch(s, p))
