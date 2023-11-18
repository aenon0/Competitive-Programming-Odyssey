class Solution:
    def shiftingLetters(self, string: str, shifts: List[List[int]]) -> str:
        pos = [0 for i in range(len(string) + 1)]
        for start, end, direction in shifts:
            if direction:
                pos[start] += 1
                pos[end + 1] -= 1
            else:
                pos[start] -= 1
                pos[end + 1] += 1
            
        _sum = 0
        ans = ""
        for indx in range(len(string)):
            _sum += pos[indx]
#             i dont understand why the following shit works tho
            ans += chr(((_sum + ord(string[indx]) - 97) % 26) + 97)
        return ans
        
        
