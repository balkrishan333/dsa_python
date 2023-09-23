class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        indexes = {}

        length, start = 0, 0

        for i, ch in enumerate(s):
            index = indexes.get(ch)
            if index is not None and index >= start:
                length = max(length, i - start)
                start = index + 1
            indexes[ch] = i

        length = max(length, len(s) - start)
        return length


sln = Solution()
s = "abcabcbb"
print(sln.lengthOfLongestSubstring(s))
