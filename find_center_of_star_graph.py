class Solution(object):
    def findCenter(self, edges):
        num_dict = defaultdict(int)
        for nums in edges:
            num_dict[nums[0]] += 1
            num_dict[nums[1]] += 1
        
        center = 0 
        _max = 1
        for key in num_dict.keys():
            if num_dict[key] > _max:
                _max = num_dict[key]
                center = key
        return center
                
