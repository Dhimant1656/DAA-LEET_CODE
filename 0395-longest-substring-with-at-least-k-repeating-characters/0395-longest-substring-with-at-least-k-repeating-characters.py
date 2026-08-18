class Solution:
    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for i, char in enumerate(s):
            if count[char] < k:
                left = self.longestSubstring(s[:i], k)
                right = self.longestSubstring(s[i + 1:], k)

                return max(left, right)

        return len(s)