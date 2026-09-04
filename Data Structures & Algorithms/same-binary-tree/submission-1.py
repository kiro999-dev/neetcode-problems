# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.isame= True
        def dfs(t1,t2):
            if(not t1 and not t2):
                return
            elif(t1 and not t2 or not t1 and t2):
                self.isame= False
                return
            if(t1.val != t2.val):
                self.isame = False
            dfs(t1.left,t2.left)
            dfs(t1.right,t2.right)
        dfs(p,q)
        return self.isame