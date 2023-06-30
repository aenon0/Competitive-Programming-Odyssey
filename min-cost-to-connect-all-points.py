class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        num_of_points = len(points)
        rep = dict()
        edges_and_cost = [ ]
        # finding every edge outta the given points
        for i in range(0, len(points)):
            # initializing the rep of every point as itself
            rep[tuple(points[i])] = tuple(points[i])

            x0, y0 = points[i]
            for j in range(i + 1, len(points)):
                x1, y1 = points[j]
                cost = abs(x1 - x0) + abs(y1 - y0)
                edges_and_cost.append((tuple(points[i]), tuple(points[j]), cost))
        # sorting the edges based on their weights
        edges_and_cost = sorted(edges_and_cost, key = lambda edge: edge[-1])

        # the union(for joining two points everynow and then) and find for 
        def find(p):
            _rep = rep[p]
            while _rep != rep[_rep]:
                _rep = rep[_rep]
            return _rep

        def union(p0, p1):
            rep0 = find(p0)
            rep1 = find(p1)
            rep[rep1] = rep0
        
        
        # unioning by looping thru the sorted list 
        min_cost = 0
        num_of_edges = 0
        for p0, p1, cost in edges_and_cost:
            # if the edge creates a cycle we dont use it to build our tree
            if find(p0) != find(p1):
                union(p0, p1)
                min_cost += cost
                num_of_edges += 1
            if num_of_edges == num_of_points:
                break
        return min_cost