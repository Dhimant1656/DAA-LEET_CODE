class Solution(object):
    def minIncrementForUnique(self, nums):
        nums.sort()
        moves = 0
        next_free = 0

        for num in nums:
            if num < next_free:
                moves += next_free - num
                next_free += 1
            else:
                next_free = num + 1

        return moves