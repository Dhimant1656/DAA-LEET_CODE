class Solution(object):
    def jump(self, nums):
        jumps = 0
        curr_end = 0
        farthest = 0
        
        for i in range(len(nums) - 1):
            if i + nums[i] > farthest:
                farthest = i + nums[i]
                
            if i == curr_end:
                jumps += 1
                curr_end = farthest
                
                if curr_end >= len(nums) - 1:
                    break
                    
        return jumps