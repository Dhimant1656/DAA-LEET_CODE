class Solution:
    def beautifulArray(self, n):
        result = [1]

        while len(result) < n:
            odd = []
            even = []

            for num in result:
                if 2 * num - 1 <= n:
                    odd.append(2 * num - 1)

                if 2 * num <= n:
                    even.append(2 * num)

            result = odd + even

        return result