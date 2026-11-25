class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1

        curr_tank = 0
        start_station = 0

        for i, (g, c) in enumerate(zip(gas, cost)):
            curr_tank += g - c
            if curr_tank < 0:
                start_station = i + 1
                curr_tank = 0

        return start_station