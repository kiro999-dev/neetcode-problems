class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backTrack(index,path):
            if(index == len(nums)):
                res.append(path[:])
                return
            path.append(nums[index])
            backTrack(index + 1,path)
            path.pop()
            backTrack(index+1,path)
        backTrack(0,[])
        return res
