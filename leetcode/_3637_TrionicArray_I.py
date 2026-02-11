from typing import List

class Solution:

    def isTrionic(self, nums: List[int]) -> bool:

        if nums[0] > nums[1]:
            return False

        i = 1
        n = len(nums)
        while i < n and nums[i-1] < nums[i]:
            i = i+1

        p = i-1

        while i < n and nums[i - 1] > nums[i]:
            i = i + 1

        q = i - 1

        while i < n and nums[i - 1] < nums[i]:
            i = i + 1

        last = i - 1

        return p > 0 and p != q and q != last and last == n-1

sln = Solution()
print(sln.isTrionic(nums=[1,3,5,4,2,6]))