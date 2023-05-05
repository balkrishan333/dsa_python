class Solution:

    def maxVowels(self, s: str, k: int) -> int:
        startindex:int = 0
        endindex: int = 0
        count: int = 0
        maxcount: int = 0
        vowels = ['a', 'e', 'i', 'o', 'u']

        for index, ch in enumerate(s):
            endindex = index
            if (endindex - startindex +1) > k:
                if s[startindex] in vowels:
                    count -= 1
                startindex += 1

            if ch in vowels:
                count += 1
                maxcount = max(maxcount, count)

        return maxcount

sln = Solution()
print(sln.maxVowels("novowels", 1))
