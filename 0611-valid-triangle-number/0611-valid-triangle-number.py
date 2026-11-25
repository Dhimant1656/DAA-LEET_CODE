class Solution(object):
    def triangleNumber(self, nums):
        nums.sort()
        count = 0

        for k in range(len(nums) - 1, 1, -1):
            left = 0
            right = k - 1
            target = nums[k]

            while left < right:
                if nums[left] + nums[right] > target:
                    count += right - left
                    right -= 1
                else:
                    left += 1

        return count