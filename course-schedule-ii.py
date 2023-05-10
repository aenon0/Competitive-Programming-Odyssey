class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph_list = defaultdict(list)
        incoming = [0] * numCourses
        for course, prerequisite in prerequisites:
            incoming[course] += 1
            graph_list[prerequisite].append(course)
        
        def bfs(queue, top_sorted):
            while queue:
                current = queue.popleft()
                top_sorted.append(current)
                for neighbor in graph_list[current]:
                    incoming[neighbor] -= 1
                    if incoming[neighbor] == 0:
                        queue.append(neighbor)
            return top_sorted
        
        queue = deque()
        for indx, dependency in enumerate(incoming):
            if dependency == 0:
                queue.append(indx)
        
        result = bfs(queue, [ ])
        if len(result) != numCourses:
            return [ ]
    
        return result