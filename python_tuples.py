if __name__ == '__main__':
    num_of_integers = int(input())
    integer_tuple = tuple(map(int, input().split()))
    print(hash(integer_tuple))
    
