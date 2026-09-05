# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.res = dict()
        self.lca = [float("+inf"),None]
        self.dfs(root,p)
        self.dfs(root,q)
        return self.lca[1]
    def dfs(self,curr:TreeNode,t):
        if(not curr):
            return
        if(curr.val in self.res):
            self.lca = [curr.val,curr]
        else:
            self.res[curr.val] = curr
        if(curr and  curr.val > t.val):
            self.dfs(curr.left,t)
        elif(curr and  curr.val < t.val):
           self.dfs(curr.right,t)
        else:
            return
    

        
