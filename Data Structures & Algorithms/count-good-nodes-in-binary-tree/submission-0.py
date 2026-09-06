# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=, Self0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.dfs(root)
        return self.count
    def dfs(self,curr,maxvalpath=float("-inf")):
        if(not curr):
            return
        if(curr.val >= maxvalpath):
            self.count +=1
            maxvalpath = curr.val
        self.dfs(curr.left,maxvalpath)
        self.dfs(curr.right,maxvalpath)
                   
