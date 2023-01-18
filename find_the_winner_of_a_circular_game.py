class Solution:
    def findTheWinner(self, num_of_friends: int, k: int) -> int:
        friends = [ i + 1 for i in range(num_of_friends) ]
        current_index = 0 
        while len(friends) > 1:
            # current_index %= num_of_friends
            # removed_index = current_index + (k - 1)
            # if removed_index >= num_of_friends:
            #     removed_index %= num_of_friends
            
            current_index += (k - 1)
            # print(current_index)
            if current_index >= len(friends):
                current_index %= len(friends)
            friends.pop(current_index)
            #is remove the function that removes using index or value...if not find one that does it with index
            # current_index += (k - 1)
        
        return friends[0]
            
        
            
        
            
