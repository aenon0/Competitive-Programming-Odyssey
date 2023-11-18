eng_studs_num = int(input())
eng_studs = set(map(int, input().split()))
french_studs_num = int(input())
french_studs = set(map(int, input().split()))

total_studs_num = len(eng_studs.union(french_studs))
print(total_studs_num)
