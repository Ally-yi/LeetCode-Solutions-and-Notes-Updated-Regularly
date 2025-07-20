"""
Problem: Longest Palindromic Substring (LeetCode #5)
Link: https://leetcode.com/problems/longest-palindromic-substring/
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=0
        r=0
        ss=""
        for i in range(len(s)):
            l,r=i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                ss = max(ss, s[l:r+1], key=len)
                l-=1
                r+=1

            l,r=i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                ss = max(ss, s[l:r+1], key=len)
                l-=1
                r+=1
                

        return ss
        
# Example usage
if __name__ == "__main__":
    solution = Solution()
    test_str = "babad"
    result = solution.longestPalindrome(test_str)
    print(result)