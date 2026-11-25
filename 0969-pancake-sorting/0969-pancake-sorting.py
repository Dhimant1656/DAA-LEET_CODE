class Solution(object):
    def pancakeSort(self, arr):
        flips = []
        for target in range(len(arr), 1, -1):
            idx = arr.index(target)
            if idx == target - 1:
                continue
            if idx > 0:
                flips.append(idx + 1)
                arr[:idx + 1] = arr[:idx + 1][::-1]
            flips.append(target)
            arr[:target] = arr[:target][::-1]
        return flips