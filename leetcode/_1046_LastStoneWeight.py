from typing import List
import queue


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = queue.PriorityQueue()

        for stone in stones:
            pq.put((-stone, stone))

        while pq.qsize() >= 2:
            w1 = pq.get()[1]
            w2 = pq.get()[1]

            if w1 != w2:
                diff = w1 - w2
                pq.put((-diff, diff))

        answer = 0
        if pq.qsize() > 0:
            answer = pq.get()[1]

        return answer


sln = Solution()
print(sln.lastStoneWeight([2, 7, 4, 1, 8, 1]))
