class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def bs(num):
            left, right = -1, len(heaters)    
            while left + 1 < right:
                mid = (left + right) // 2
                if heaters[mid] > num:
                    right = mid
                else:
                    left = mid
            return left

        
        min_distance = [inf] * len(houses)

        for i, house in enumerate(houses):
            idx = bs(house)
            min_distance[i] = min(min_distance[i], abs(heaters[idx] - houses[i]))
            if idx - 1 >= 0:
                min_distance[i] = min(min_distance[i], abs(heaters[idx - 1] - houses[i]))
            if idx + 1 < len(heaters):
                min_distance[i] = min(min_distance[i], abs(heaters[idx + 1] - houses[i]))
        print(min_distance)
        return max(min_distance)