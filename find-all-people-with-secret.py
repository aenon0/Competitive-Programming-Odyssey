class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        adj_list = defaultdict(list)
        adj_list[0].append((firstPerson, 0))
        adj_list[firstPerson].append((0, 0))
        for person1, person2, time in meetings:
            adj_list[person1].append((person2, time))
            adj_list[person2].append((person1, time))
        
        
        def bfs(person, time):
            queue = deque([(person, time)])
            visited = set()
            gossipers = set([0, person])
            while queue:
                curr_person, curr_time = queue.popleft()
                for nxt_person, nxt_time in adj_list[curr_person]:
                    if nxt_time >= curr_time and (curr_person, nxt_person) not in visited and (nxt_person, curr_person) not in visited:
                        visited.add((curr_person, nxt_person))
                        queue.append((nxt_person, nxt_time))
                        gossipers.add(nxt_person)
            

            return list(gossipers)

        res = bfs(0, 0)
        return res