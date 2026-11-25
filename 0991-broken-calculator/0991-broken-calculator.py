class Solution(object):
    def brokenCalc(self, startValue, target):
        if startValue >= target:
            return startValue - target
        if target & 1:
            return 1 + self.brokenCalc(startValue, target + 1)
        return 1 + self.brokenCalc(startValue, target >> 1)