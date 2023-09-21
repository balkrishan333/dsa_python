from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        length = len(nums1) + len(nums2)
        median_index = int(length / 2)
        i, j, curr = 0, 0, 0
        median = []

        while i < len(nums1) or j < len(nums2) or curr < median_index:
            if i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:
                    median.append(nums1[i])
                    i += 1
                    curr += 1
                else:
                    median.append(nums2[j])
                    j += 1
                    curr += 1
            elif i < len(nums1):
                median.append(nums1[i])
                i += 1
                curr += 1
            elif j < len(nums2):
                median.append(nums2[j])
                j += 1
                curr += 1

        if length % 2 == 0:
            return (median[median_index] + median[median_index-1]) / 2

        return median[median_index]


sln = Solution()
nums1 = []
nums2 = [2, 3]
print(sln.findMedianSortedArrays(nums1, nums2))
