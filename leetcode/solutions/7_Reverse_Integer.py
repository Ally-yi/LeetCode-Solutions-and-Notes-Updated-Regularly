"""
Problem: Reverse Integer (LeetCode #7)
Link: https://leetcode.com/problems/reverse-integer/
"""
class Solution:
    def reverse(self, x: int) -> int:
        """
        Reverse digits of a 32-bit signed integer.
        If it overflows, return 0.
        """
        INT_MAX = 2**31 - 1      # 2147483647
        INT_MIN = -2**31         # -2147483648

        num = 0                  # Store reversed number
        sign = 1 if x >= 0 else -1  # Determine the sign
        x = abs(x)               # Work with the absolute value of x

        while x != 0:
            digit = x % 10       # Get the last digit
            x = x // 10          # Remove the last digit
            num = num * 10 + digit  # Append digit to reversed number

            # Check for overflow after applying sign
            if num * sign > INT_MAX or num * sign < INT_MIN:
                return 0

        return num * sign


# Test cases
if __name__ == "__main__":
    solution = Solution()
    test=-123  
    print(solution.reverse(test))
