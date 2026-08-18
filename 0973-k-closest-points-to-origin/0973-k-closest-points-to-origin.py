import heapq

class Solution:
    def kClosest(self, points, k):
        heap = []

        for x, y in points:
            distance = x * x + y * y

            heapq.heappush(heap, (-distance, x, y))

            if len(heap) > k:
                heapq.heappop(heap)

        return [[x, y] for _, x, y in heap]