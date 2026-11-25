class Solution(object):
    def maximumSwap(self, num):
        digits = list(str(num))
        last_pos = {int(d): i for i, d in enumerate(digits)}

        for i, d in enumerate(digits):
            curr = int(d)
            for candidate in range(9, curr, -1):
                if last_pos.get(candidate, -1) > i:
                    swap_idx = last_pos[candidate]
                    digits[i], digits[swap_idx] = digits[swap_idx], digits[i]
                    return int("".join(digits))

        return num