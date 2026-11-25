from collections import Counter

class Solution(object):
    def numRabbits(self, answers):
        total = 0

        for ans, count in Counter(answers).items():
            group_size = ans + 1
            groups = (count + ans) // group_size
            total += groups * group_size

        return total