import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:


        heap = [-x for x in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y, x = heapq.heappop(heap), heapq.heappop(heap)

            left = y - x
            if left < 0:
                heapq.heappush(heap,left)
            
        return abs(heap[0]) if heap else 0
        