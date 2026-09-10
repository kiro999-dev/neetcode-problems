import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)
        if(len(stones) == 1):
            return stones [0]
        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            if(x > y):
                heapq.heappush_max(stones,abs(x - y))
        if(len(stones) == 0):
            return 0
        return stones[0]