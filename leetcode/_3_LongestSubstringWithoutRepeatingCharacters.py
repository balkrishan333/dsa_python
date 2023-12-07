class Solution:

    if __name__ == "__main__":
        print("Running _3_LongestSubstringWithoutRepeatingCharacters.py")
    def lengthOfLongestSubstring(self, s: str) -> int:
        symbols = [-1]*255

        start, max_len = 0, 0

        for i in range(len(s)) :
            char = s[i]
            char_to_int = ord(char)
            curr_index = symbols[char_to_int]
            if curr_index != -1:
                if curr_index >= start:
                    max_len = max(max_len, i-start)
                    start = curr_index +1
            symbols[char_to_int] = i

        return max(max_len, len(s)- start)

sln = Solution()
print("Max length : ", sln.lengthOfLongestSubstring("abcabcbb"))
