
"""
Problem: Group Anagrams (LeetCode #49)
Link: https://leetcode.com/problems/group-anagrams/
"""

from collections import defaultdict  
from typing import List             

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to store grouped anagrams
        # Key: sorted version of a word
        # Value: list of words that are anagrams of each other
        anagrams = defaultdict(list)

        for word in strs:
            # Sort the characters in the word and use it as a key
            # Example: "tea" -> "aet"
            key = "".join(sorted(word))

            # Append the original word to the list corresponding to the sorted key
            anagrams[key].append(word)

        # Return all the grouped anagrams as a list of lists
        return list(anagrams.values())


# --------------------- Test Cases ---------------------
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [""],
        ["a"],
        ["abc", "bca", "cab", "bac", "acb", "cba"],
        ["abcd", "dcba", "abdc", "aabb", "baba", "bbaa"],
    ]

    for i, strs in enumerate(test_cases, 1):
        print(f"Test Case {i}: {strs}")
        result = solution.groupAnagrams(strs)
        print("Grouped Anagrams:", result)
        print("-" * 40)
