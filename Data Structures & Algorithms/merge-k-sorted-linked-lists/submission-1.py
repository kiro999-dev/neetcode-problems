# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import itertools

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy
        h = []
        counter = itertools.count()
        pointers = list(lists)
        for i in range(len(lists)):
            if(pointers[i]):
                heapq.heappush(h, [pointers[i].val,next(counter),pointers[i]])
                pointers[i] = pointers[i].next
        while h:
            val,c,node = heapq.heappop(h)
            temp.next = node
            temp = temp.next
            if(node.next):
                heapq.heappush(h, [node.next.val,next(counter),node.next])
        return dummy.next
           
           
           
        
        