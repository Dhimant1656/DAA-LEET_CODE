class Solution:
    def topKFrequent(self, nums, k):
        count = {}

        # Count frequency of each number
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Bucket: index = frequency
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        # Get k most frequent elements
        result = []

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k:
                    return result