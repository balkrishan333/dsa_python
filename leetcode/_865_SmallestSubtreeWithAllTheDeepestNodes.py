from typing import Optional
from xxlimited import new

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Result:
    def __init__(self, node: Optional[TreeNode], depth: int):
        self.node = node
        self.depth = depth
        
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        result = self.dfs(root)
        return result.node
    
    def dfs(self, node: Optional[TreeNode]) -> Result:
        if not node:
            return Result(None, 0)
        
        left_result = self.dfs(node.left)
        right_result = self.dfs(node.right)
        
        if left_result.depth > right_result.depth:
            return Result(left_result.node, left_result.depth + 1)
        elif right_result.depth > left_result.depth:
            return Result(right_result.node, right_result.depth + 1)
        else:
            return Result(node, left_result.depth + 1)
        
sln = Solution()
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)

print(sln.subtreeWithAllDeepest(root).val)  # Output should be 2