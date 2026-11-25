class Solution(object):
    def smallestRangeII(self, nums, k):
        nums.sort()
        min_val = nums[0]
        max_val = nums[-1]
        ans = max_val - min_val

        for i in range(len(nums) - 1):
            high = max_val - k if max_val - k > nums[i] + k else nums[i] + k
            low = min_val + k if min_val + k < nums[i + 1] - k else nums[i + 1] - k
            if high - low < ans:
                ans = high - low

        return ans
        