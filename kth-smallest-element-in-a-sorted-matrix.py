class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = [ ]
        heapq.heapify(heap)
        for row in matrix:
            for item in row:
                heapq.heappush(heap, item)
        
        while k:
            curr = heapq.heappop(heap)
            k -= 1
        
        return curr