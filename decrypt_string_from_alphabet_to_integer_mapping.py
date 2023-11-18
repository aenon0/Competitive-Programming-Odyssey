class Solution:
    def freqAlphabets(self, s: str) -> str:
        decrypted_string = ""
        dic = {
            1: "a",
            2: "b",
            3: "c",
            4: "d",
            5: "e",
            6: "f",
            7: "g",
            8: "h",
            9: "i",
            "10#": "j",
            "11#": "k",
            "12#": "l",
            "13#": "m",
            "14#": "n",
            "15#": "o",
            "16#": "p",
            "17#": "q",
            "18#": "r",
            "19#": "s",
            "20#": "t",
            "21#": "u",
            "22#": "v",
            "23#": "w",
            "24#": "x",
            "25#": "y",
            "26#": "z"
        }
        
        left_hash_index = 0 
        right_hash_index = 0
        index = 0
        while index < len(s):
            if  index+ + 2 <= len(s)-1 and s[index+2] == '#':
                left_hash_index = index
                right_hash_index = index + 2
                decrypted_string += dic.get(s[left_hash_index : right_hash_index+1],'')
                index += 3
                continue
            else:
                decrypted_string += dic.get(int(s[index]),'')
            if  index + 2 == len(s) - 1 and s[index+2] == '#':
                break
            index += 1
        return decrypted_string
