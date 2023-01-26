class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left_ptr =  0 
        right_ptr = len(people) - 1
        min_boats = 0 
        while left_ptr <= right_ptr:
            if people[left_ptr] + people[right_ptr] == limit or  people[left_ptr] + people[right_ptr] < limit:
                left_ptr += 1
                right_ptr -= 1
                min_boats += 1
            elif people[left_ptr] + people[right_ptr] > limit:
                right_ptr -= 1
                min_boats += 1
        
        return min_boats
           
        
