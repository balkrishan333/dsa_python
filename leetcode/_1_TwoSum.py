from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        index_map = {}
        answer = []
        for i, num in enumerate(nums):
            if (target - num) in index_map:
                index = index_map[target - num]
                answer.append(i)
                answer.append(index)
                break
            else:
                index_map[num] = i

        return answer


sln = Solution()
print(sln.twoSum(nums=[2, 7, 11, 15], target=9))
