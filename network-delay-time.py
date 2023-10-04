class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for node1, node2, time in times:
            graph[node1].append((time, node2))


        heap = [(0, k)]
        heapq.heapify(heap)
        res = [inf] * n
        visited = set()
        while heap:
            time, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)

            for t, neighbor in graph[node]:
                if neighbor not in visited and t + time < res[neighbor - 1]:
                    res[neighbor - 1] = time + t
                    heapq.heappush(heap, (time + t, neighbor))
        print(res)
        if inf in res:
            res.remove(inf)

        return max(res) if max(res)!= inf else -1