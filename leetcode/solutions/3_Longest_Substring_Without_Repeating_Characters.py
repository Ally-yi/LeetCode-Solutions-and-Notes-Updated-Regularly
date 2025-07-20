"""
Problem: Longest Substring Without Repeating Characters (LeetCode #3)
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        a=set()
        maxL=0
        left=0
        for right in range(len(s)):
            while s[right] in a:
                a.remove(s[left])
                left+=1
            a.add(s[right])
            maxL=max(maxL,right-left+1)
        return maxL

# Example usage
if __name__ == "__main__":
    solution = Solution()
    test_str = "abcabcbb"
    result = solution.lengthOfLongestSubstring(test_str)
    print(result)