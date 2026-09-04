# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalance = True
        if(not root):
            return True
        def dfs(curr)->int:
            if(not curr):
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)
            if(abs(right - left) > 1):
                self.isBalance = False
            return max(right,left)+1
        self.left =  dfs(root.left)
        self.right = dfs(root.right)
        if(abs(self.right - self.left) > 1):
            self.isBalance = False
        return self.isBalance
