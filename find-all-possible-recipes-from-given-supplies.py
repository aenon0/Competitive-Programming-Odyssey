class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegrees = [0] * len(recipes)
        for indx, ingredient in enumerate(ingredients):
            for i in ingredient:
                graph[i].append(recipes[indx])
                indegrees[indx] += 1
            
        recipes_set = set(recipes)
        
        def bfs(queue, visited, possible_recipes):
            while queue:
                curr = queue.popleft()
                visited.add(curr)
                for neighbor in graph[curr]:
                    indegrees[recipes.index(neighbor)] -= 1
                    if neighbor not in visited and indegrees[recipes.index(neighbor)] == 0:
                        queue.append(neighbor)
                        visited.add(neighbor)
                        if neighbor in recipes:
                            possible_recipes.append(neighbor)
                            
            return possible_recipes
        
        return bfs(deque(supplies), set(), [ ])