"""
Problem: String to Integer(LeetCode #8)
Link: https://leetcode.com/problems/string-to-integer-atoi/
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        """
        Convert a string to a 32-bit signed integer (similar to C/C++'s atoi).
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        num_str = ""      # Store the numeric part of the string
        n = len(s)
        sign_seen = False
        sign = 1
        i = 0

        # 1. Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # 2. Read optional sign and digits
        while i < n:
            c = s[i]
            if c == '+' and not sign_seen and num_str == "":
                sign = 1
                sign_seen = True
            elif c == '-' and not sign_seen and num_str == "":
                sign = -1
                sign_seen = True
            elif c.isdigit():
                num_str += c
            else:
                break
            i += 1

        # 3. Return 0 if no digits found
        if num_str == "":
            return 0

        # 4. Convert to integer and apply sign
        num = int(num_str) * sign

        # 5. Clamp to 32-bit signed integer range
        if num > INT_MAX:
            return INT_MAX
        if num < INT_MIN:
            return INT_MIN
        return num

# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    test = " -04193 with words"
    result = solution.myAtoi(test)
    print(result)
