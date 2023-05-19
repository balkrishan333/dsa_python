from typing import List


class Solution:

    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors: List[int] = [None] * len(graph)

        for index, adjacencyGraph in enumerate(graph):
            if colors[index] is None and not self.dfs(index, colors, 0, graph):
                return False
        return True

    def dfs(self, node:int, colors:List[int], color:int, graph:List[List[int]]) -> bool:
        if colors[node] is not None:
            return colors[node] == color

        colors[node] = color
        next_color = 1
        if color == 1:
            next_color = 0

        for adjacent in graph[node]:
            if not self.dfs(adjacent, colors, next_color, graph):
                return False
        return True

sln = Solution()
print(sln.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))
