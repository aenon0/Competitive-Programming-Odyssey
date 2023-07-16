class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         bucket sort 
        bucket = [[] for i in range(len(nums) + 1)]
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        for num in freq.keys():
            bucket[freq[num]].append(num)
        
        ans = [ ]
        for idx in range(len(bucket) - 1, -1, -1):
            if k == 0:
                break
            if bucket[idx]:
                curr = bucket[idx][0 : k]
                ans.extend(curr)
                k -= len(curr)
                
        return ans