import textwrap

def wrap(string, max_width):
    paragraph = ""

    right_index = 0 
    left_index = 0
    
    for index in range(0, len(string), max_width):
        right_index += max_width  #right = 2,4,6... if max_width = 2
        paragraph += (string[left_index: right_index] + "\n")
        left_index = right_index
                   
    return paragraph

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
