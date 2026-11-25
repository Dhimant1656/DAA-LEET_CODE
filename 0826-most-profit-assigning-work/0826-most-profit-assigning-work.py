class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        max_ability = max(worker)
        best_profit = [0] * (max_ability + 1)

        for d, p in zip(difficulty, profit):
            if d <= max_ability and p > best_profit[d]:
                best_profit[d] = p

        for i in range(1, max_ability + 1):
            if best_profit[i - 1] > best_profit[i]:
                best_profit[i] = best_profit[i - 1]

        return sum(best_profit[w] for w in worker)