class Solution:
    def addSpaces(self, string: str, spaces: List[int]) -> str:
        modified_string = ""
        left_index = 0
        for index in range(len(spaces)):
            if spaces[index] == 0:
                modified_string += " "
            else:
                modified_string += string[left_index: spaces[index]] + " "
                left_index = spaces[index] 
        modified_string += string[left_index: ]
        return modified_string
        
            
