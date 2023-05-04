from typing import List


class Solution:

    # initial implementation, very long. Refer below implementation for compact code which does the same thing.
    def findDifference_1(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        dict1 = {}
        dict2 = {}
        list1 = []
        list2 = []

        answer: list[list[int]] = [list1, list2]

        for num in nums1:
            dict1[num] = True

        for num in nums2:
            dict2[num] = True
            if num not in dict1:
                if num not in list2:
                    list2.append(num)

        for num in nums1:
            if num not in dict2:
                if num not in list1:
                    list1.append(num)

        return answer

    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        return list(set1.difference(set2)), list(set2.difference(set1))


sln = Solution()
answer = sln.findDifference([1, 2, 3, 3], [1, 1, 2, 2])
print(answer)
