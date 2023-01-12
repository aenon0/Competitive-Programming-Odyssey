class Solution:
    def reverseString(self, letter_list: List[str]) -> None:
        right_index = len(letter_list) - 1
        left_index = 0 
        while(left_index < right_index):
            letter_list[left_index], letter_list[right_index] = letter_list[right_index], letter_list[left_index] 
            right_index -= 1 
            left_index += 1
        return letter_list
        
