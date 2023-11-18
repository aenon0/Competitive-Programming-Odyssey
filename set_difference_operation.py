eng_studs_num = int(input())
eng_studs = set(map(int, input().split()))
french_studs_num = int(input())
french_studs = set(map(int, input().split()))

only_eng_studs_num = len(eng_studs.difference(french_studs))
print(only_eng_studs_num)
