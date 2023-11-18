def split_and_join(line):
    # write your code here
    ans= ""
    index=0
    for char in line:
        if char != " ":
            ans+= char
        else: 
            ans+="-"
            index+=1
    return ans 
        
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
