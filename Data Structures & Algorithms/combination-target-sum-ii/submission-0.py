class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtracking(i,total,path):
            if(total == target):
                res.append(path[:])
                return
            if(total > target or i >= len(candidates)):
                return
           
            path.append(candidates[i])
            backtracking(i+1,total+candidates[i],path)
            path.pop()
            while i + 1 < len(candidates) and candidates[i]==candidates[i+1]:
                i += 1
            backtracking(i+1,total,path)

        backtracking(0,0,[])
        return res