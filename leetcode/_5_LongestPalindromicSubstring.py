class Solution:
    def longestPalindrome(self, s: str) -> str:

        length, start, end = 0,0,0
        for i in range(len(s)):
            odd = self.expand(s, i, i)
            even = self.expand(s, i, i+1)

            length = max(odd, even)

            if length > end - start:
                start = i - (length-1)//2
                end = i + length // 2

        return s[start: end+1]

    def expand(self, s: str, left:int, right:int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left = left-1
            right = right+1

        return (right-1) - (left+1) +1

sln = Solution()
print(sln.longestPalindrome("cbbd"))