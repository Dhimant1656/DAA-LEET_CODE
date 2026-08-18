class Solution:
    def countElements(self, nums, k):
        if k == 0:
            return len(nums)

        nums.sort()

        threshold = nums[len(nums) - k]
        count = 0

        for num in nums:
            if num < threshold:
                count += 1

        return count