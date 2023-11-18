class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        nums = [0] * len(nums1)
        self.pair = 0 
        for indx in range(len(nums)):
            nums[indx] = nums1[indx] - nums2[indx]
        
        def binary_search(num, arr):
            left = -1
            right = len(arr)
            while left + 1 < right:
                mid = (left + right) // 2
                if arr[mid] < num:
                    left = mid
                else:
                    right = mid
                    
            return right
                    
                
        def merge(left_side, right_side):
            result = [ ]
            # print(left_side,right_side)
            for num in left_side:
                # print(num, diff)
                indx = binary_search(num - diff, right_side)
                if indx != -1:
                    self.pair += len(right_side) - indx
            
            p1 = 0 
            p2 = 0 
            while p1 < len(left_side)  and p2 < len(right_side):
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
        return self.pair
        
        
        
        
            
       
