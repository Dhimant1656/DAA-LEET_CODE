class Solution(object):
    def partitionLabels(self, s):
        last_index = {char: i for i, char in enumerate(s)}
        partitions = []
        start = 0
        end = 0

        for i, char in enumerate(s):
            if last_index[char] > end:
                end = last_index[char]

            if i == end:
                partitions.append(end - start + 1)
                start = i + 1

        return partitions