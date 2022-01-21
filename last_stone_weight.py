# Last Stone Weight
# https://leetcode.com/problems/last-stone-weight/


from heapq import heappush, heappop
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap: List[int] = []

        for w in stones:
            heappush(heap, -w)  # heapq implements minheap

        while len(heap) > 1:
            x: int = heappop(heap)
            y: int = heappop(heap)

            if x < y:
                heappush(heap, x - y)
            elif y < x:
                heappush(heap, y - x)

        if len(heap) == 1:
            return -heap[0]
        else:
            return 0
