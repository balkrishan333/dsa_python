class Solution:
    def reverse(self, x: int) -> int:
        answer = 0

        int_max = 2**31-1
        int_min = -2**31

        sign = -1 if x < 0 else 1
        x = abs(x)
        while x != 0:
            bit = x % 10
            x = x//10

            if answer > int_max/10 or answer < int_min/10:
                return 0

            answer = answer * 10 + bit
        return answer * sign

sln = Solution()
print(sln.reverse(-123))