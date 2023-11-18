class Solution:
    def interpret(self, command: str) -> str:
        ans=""
        for index in range(len(command)):
            if command[index]=="G":
                ans+= "G"
            elif command[index: index+4 ]== "(al)":
                ans+="al"
            elif command[index: index+2 ]== "()":
                ans+="o"
        return ans
