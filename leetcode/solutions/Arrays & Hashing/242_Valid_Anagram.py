"""
Problem: valid-anagram (LeetCode #242)
Link: https://leetcode.com/problems/valid-anagram
"""

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Return True if the frequency of each character in both strings is the same
        return Counter(s) == Counter(t)
        
        # Alternatively, use the sorting method:
        # return sorted(s) == sorted(t)


# --------- Test cases ---------
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ("listen", "silent"),
        ("anagram", "nagaram"),
        ("rat", "car"),
        ("aabbcc", "abcabc"),
        ("hello", "bello"),
        ("", ""),
        ("a", "a"),
        ("a", "b"),
    ]

    for s, t in test_cases:
        result = solution.isAnagram(s, t)
        print(result)
