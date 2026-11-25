from collections import Counter

class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False

        counts = Counter(hand)

        for start in sorted(counts):
            need = counts[start]
            if need > 0:
                for card in range(start, start + groupSize):
                    if counts[card] < need:
                        return False
                    counts[card] -= need

        return True