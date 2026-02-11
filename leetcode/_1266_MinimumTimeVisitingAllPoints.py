from typing import List

class Solution:

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i, point in enumerate(points):
            currX = point[0]
            currY = point[1]

            if i < len(points)-1:
                next_point = points[i+1]
                targetX = next_point[0]
                targetY = next_point[1]

                #using chess distance formula
                ans += max(abs(currX-targetX), abs(currY-targetY))

        return ans

sln = Solution()
points = [[1,1],[3,4],[-1,0]]
print(sln.minTimeToVisitAllPoints(points))
