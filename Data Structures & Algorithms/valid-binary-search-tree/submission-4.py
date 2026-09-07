# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.array = []
        self.dfs(root)
        is_sorted = all(self.array [i] < self.array [i+1] for i in range(len(self.array ) - 1))
        return is_sorted

    def dfs(self,curr):
        if(not curr):
            return
        self.dfs(curr.left)
        self.array.append(curr.val)
        self.dfs(curr.right)
       
            