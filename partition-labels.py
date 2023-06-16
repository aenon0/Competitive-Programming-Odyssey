class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurence = dict()
        for idx, char in enumerate(s):
            last_occurence[char] = idx
            
        partitions = [ ]
        start = end = 0 
        for idx, char in enumerate(s):
            end = max(end, last_occurence[char])
            if idx == end:
                partitions.append(idx - start + 1)
                start = end + 1
        return partitions