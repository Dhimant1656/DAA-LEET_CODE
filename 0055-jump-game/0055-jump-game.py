class Solution(object):
    def canJump(self, nums):
        max_reach = 0
        last_index = len(nums) - 1
        
        for i in range(len(nums)):
            if i > max_reach:
                return False
            
            if i + nums[i] > max_reach:
                max_reach = i + nums[i]
                
            if max_reach >= last_index:
                return True
                
        return True