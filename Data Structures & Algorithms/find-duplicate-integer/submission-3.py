class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if(slow == fast):
                break
        s2 = 0
        while s2 != slow:
            s2 = nums[s2]
            slow = nums[slow]
            
        return slow