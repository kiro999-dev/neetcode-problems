import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heapmax = []
        for num in nums:
            heapq.heappush(self.heapmax,-num)

    def add(self, val: int) -> int:
        k = self.k
        heapq.heappush(self.heapmax,-val)
        heap_copy = self.heapmax[:]      
        kthLarg = val
        while(k):
            kthLarg = -heapq.heappop(heap_copy)
            k-=1
        return kthLarg