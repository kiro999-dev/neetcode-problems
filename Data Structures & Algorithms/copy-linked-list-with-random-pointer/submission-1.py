"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head 
        nodeMap = dict()
        while temp:
            nodeMap[temp] = Node(temp.val)
            temp = temp.next
        temp = head
        while temp:
            nodeMap[temp].next = nodeMap.get(temp.next,None)
            nodeMap[temp].random = nodeMap.get(temp.random,None)
            temp = temp.next
        return nodeMap.get(head,None)