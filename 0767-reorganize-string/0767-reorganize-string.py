from collections import Counter

class Solution(object):
    def reorganizeString(self, s):
        n = len(s)
        counts = Counter(s)
        max_char, max_freq = counts.most_common(1)[0]

        if max_freq > (n + 1) // 2:
            return ""

        res = [""] * n
        idx = 0

        for _ in range(max_freq):
            res[idx] = max_char
            idx += 2

        del counts[max_char]

        for char, freq in counts.items():
            for _ in range(freq):
                if idx >= n:
                    idx = 1
                res[idx] = char
                idx += 2

        return "".join(res)