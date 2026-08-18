class Solution:
    def wiggleSort(self, nums):
        nums.sort()

        n = len(nums)
        mid = (n - 1) // 2
        high = n - 1

        result = [0] * n

        for i in range(n):
            if i % 2 == 0:
                result[i] = nums[mid]
                mid -= 1
            else:
                result[i] = nums[high]
                high -= 1

        nums[:] = result