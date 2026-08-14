class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upperbound = max(piles)
        res = 1
        l = 1
        r = upperbound
       
        while l <= r :
             k = (l+r) // 2
             totaltime = 0
             for pile in piles:
                totaltime +=  math.ceil(float(pile) / k)
                
             if(totaltime <= h):
                    res = k
                    r = k - 1
             else:
                    l = k + 1
        return res