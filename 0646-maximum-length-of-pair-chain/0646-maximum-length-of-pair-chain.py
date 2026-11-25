class Solution(object):
    def findLongestChain(self, pairs):
        pairs.sort(key=lambda x: x[1])
        curr_end = float('-inf')
        chain_len = 0

        for left, right in pairs:
            if left > curr_end:
                curr_end = right
                chain_len += 1

        return chain_len