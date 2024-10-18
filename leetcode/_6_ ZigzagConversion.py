class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if len(s) < 2 or numRows == 1:
            return s

        result = ''
        for row in range(numRows):
            for i in range(row, len(s), 2*(numRows-1)):
                result += s[i]
                if row != 0 and row != numRows-1 and i+2*(numRows-1) - 2*row < len(s):
                    result += s[i+2*(numRows-1) - 2*row]

        return result

sln = Solution()
print(sln.convert('PAYPALISHIRING', 3))