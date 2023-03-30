class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.reverse_pairs =  0
        def binary_search(arr, key):
            left = -1
            right = len(arr)
            while left + 1 < right:
                mid = (left + right) // 2
                
                if 2 * (arr[mid]) >= key: 
                    right = mid
                else:
                    left = mid
                    
            return left + 1
        
        def merge(left_side, right_side):
            for indx in range(len(left_side)):
                
                i = binary_search(right_side, left_side[indx])
                self.reverse_pairs += (i)
            
            p1 = 0 
            p2 = 0 
            result = [ ]
            while p1 < len(left_side) and p2 < len(right_side):
                if left_side[p1] <= right_side[p2]:
                    result.append(left_side[p1])
                    p1 += 1
                else:
                    result.append(right_side[p2])
                    p2 += 1
            result.extend(left_side[p1 : ])
            result.extend(right_side[p2 : ])
            return result
                    
        
        def merge_sort(nums, left, right):
            if left == right:
                return [nums[left]]
            
            mid = (left + right) // 2
            left_side = merge_sort(nums, left, mid)
            right_side = merge_sort(nums, mid + 1, right)
            
            return merge(left_side, right_side)
        
        merge_sort(nums, 0, len(nums) - 1)
        return self.reverse_pairs
