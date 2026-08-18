class Solution:
    def kthLargestNumber(self, nums, k):
        nums.sort(key=lambda x: (len(x), x), reverse=True)
        return nums[k - 1]