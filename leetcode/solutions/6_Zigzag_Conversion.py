"""
Problem: Zigzag Conversion (LeetCode #6)
Link: https://leetcode.com/problems/zigzag-conversion/
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Convert a string to its Zigzag form with numRows rows and return the result.
        """
        if numRows == 1 or numRows >= len(s):
            return s

        a = [''] * numRows  # Create a list to hold strings for each row
        going_down = False  # Direction flag
        current_row = 0     # Start from the first row

        for char in s:
            a[current_row] += char  # Append current character to the correct row
            # Change direction at the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            # Move up or down
            current_row += 1 if going_down else -1

        return ''.join(a)  # Concatenate all rows


# Example usage
if __name__ == "__main__":
    solution = Solution()
    s = "PAYPALISHIRING"
    numRows = 3
    result = solution.convert(s, numRows)
    print(result)
