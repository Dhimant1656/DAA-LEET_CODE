class Solution(object):
    def largestNumber(self, nums):
        str_nums = [str(num) for num in nums]
        str_nums.sort(key=lambda x: x * 10, reverse=True)

        if str_nums[0] == "0":
            return "0"

        return "".join(str_nums)