class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backTrack(index,path,sumNum):
            if(sumNum >= target or len(nums) == index):
                if(sumNum == target):
                    res.append(path[:])
                return
            path.append(nums[index])
            backTrack(index,path,sumNum+nums[index])
            path.pop()
            backTrack(index+1,path,sumNum)
            
        backTrack(0,[],0)
        return res