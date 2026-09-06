# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        resList = []
        if(not root):
            return resList
            
        q.append(root)
        resList.append(root.val)
        sideVal = 0
        while (q):
            sideVal = float("+inf")
            for _ in range(len(q)):
                node = q.popleft()
                if(node):
                    q.append(node.left)
                    q.append(node.right)
                    if(node.right):
                        sideVal = node.right.val
                    elif(node.left):
                        sideVal = node.left.val
            if(sideVal != float("+inf")):
                resList.append(sideVal)
        return resList