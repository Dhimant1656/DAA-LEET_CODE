class Solution(object):
    def maxDistance(self, arrays):
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_dist = 0

        for arr in arrays[1:]:
            curr_min = arr[0]
            curr_max = arr[-1]

            if max_val - curr_min > max_dist:
                max_dist = max_val - curr_min
            if curr_max - min_val > max_dist:
                max_dist = curr_max - min_val

            if curr_min < min_val:
                min_val = curr_min
            if curr_max > max_val:
                max_val = curr_max

        return max_dist