class Solution(object):
    def maximalNetworkRank(self, n, roads):
        city_roads = defaultdict(list)
        for i in range(len(roads)):
            city_roads[roads[i][0]].append(i)
            city_roads[roads[i][1]].append(i)
        
        max_rank = 0 
        for key in city_roads.keys():
            for key1 in city_roads.keys():
                if key != key1:
                    temp = set(city_roads[key]).union(set(city_roads[key1]))
                    max_rank = max(max_rank, len(temp))   
        # print(city_roads)
        return max_rank
        
