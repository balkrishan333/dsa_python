from typing import List
from queue import PriorityQueue
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        pq = PriorityQueue()

        for index, row in enumerate(mat):
            count = 0
            for val in row:
                if val == 1:
                    count = count+1
            pq.put([count, index])

        result = []
        for i in range(0, k):
            result.append(pq.get()[1])

        return result

mat = [[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]]
k = 3

sln = Solution()
answer = sln.kWeakestRows(mat, k)
print(answer)