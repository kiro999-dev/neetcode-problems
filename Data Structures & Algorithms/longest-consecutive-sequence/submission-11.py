class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxl = 0
        l = 0
        for num in numsSet:
            if((num -1) not in numsSet ):
                l = 1
                while(num +l) in numsSet:
                    l+=1
                maxl = max(l,maxl)

        return maxl
            