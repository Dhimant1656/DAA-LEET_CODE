class Solution(object):
    def findUnsortedSubarray(self, nums):
        n = len(nums)
        max_seen = nums[0]
        min_seen = nums[-1]
        right = -1
        left = 0

        for i in range(1, n):
            if nums[i] < max_seen:
                right = i
            else:
                max_seen = nums[i]

        for i in range(n - 2, -1, -1):
            if nums[i] > min_seen:
                left = i
            else:
                min_seen = nums[i]

        return right - left + 1 if right != -1 else 0