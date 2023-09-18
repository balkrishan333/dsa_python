import sys
from typing import List
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        length = len(points)
        edges, curr, result = 0,0,0
        dist_arr = [sys.maxsize] * length
        visited = [False] * length
        visited[0] = True

        while edges < length-1:
            min_edge = sys.maxsize
            next_node = -1
            for i, point in enumerate(points):
                if not visited[i]:
                    cost = abs(points[curr][0] - point[0]) + abs(points[curr][1] - point[1])
                    dist_arr[i] = min(dist_arr[i], cost)

                    if dist_arr[i] < min_edge:
                        min_edge = dist_arr[i]
                        next_node = i

            result += min_edge
            edges = edges +1
            curr = next_node
            visited[curr] = True

        return result

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
sln = Solution()
print(sln.minCostConnectPoints(points))