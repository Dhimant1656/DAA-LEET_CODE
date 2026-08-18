class Solution:
    def majorityElement(self, nums):

        count = 0
        winner = 0

        for num in nums:

            if count == 0:
                winner = num
                count = 1

            elif num == winner:
                count += 1

            else:
                count -= 1

        return winner