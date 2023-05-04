class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_dict = defaultdict(int)
        for word in words:
            word_dict[word] += 1
        heap = [ ]
        heapq.heapify(heap)
        for key in word_dict.keys():
            heapq.heappush(heap, (-1 * word_dict[key],  (key)))
        ans = [ ]
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans