class Solution:
    def smallestTrimmedNumbers(self, nums, queries):
        answer = []

        for k, trim in queries:
            indices = list(range(len(nums)))

            indices.sort(key=lambda i: (nums[i][-trim:], i))

            answer.append(indices[k - 1])

        return answer