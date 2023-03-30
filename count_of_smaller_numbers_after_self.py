class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.counts = [0] * len(nums)
        for indx in range(len(nums)):
            nums[indx] = [indx, nums[indx]]        
        
        def binary_search(arr, key):
            left = -1 
            right = len(arr)
            while left + 1 < right:
                mid = (left + right) // 2
                if arr[mid][1] >= key:
                    right = mid
                else:
                    left = mid
            return right
        
        def merge(left_side, right_side):             
            # print(left_side, right_side, self.counts)
            for indx in range(len(left_side)):
                count = 0 
                i = binary_search(right_side, left_side[indx][1])
                count += i
                # print(indx, left_side,i, right_side,)
                self.counts[left_side[indx][0]] += count 
            
            p1 = 0 
            p2 = 0 
            result = [ ]
            while p1 < len(left_side) and p2 < len(right_side):
                if left_side[p1][1] <= right_side[p2][1]:
                    result.append(left_side[p1])
                    p1 += 1
                else: 
                    result.append(right_side[p2])
                    p2 += 1 
                    
            result.extend(left_side[p1 : ])
            result.extend(right_side[p2 : ])
            return result
                        
                
        def merge_sort(arr, left, right):
            if left == right:
                return [arr[left]]
            
            mid = (left + right) // 2
            left_side = merge_sort(arr, left, mid)
            right_side = merge_sort(arr, mid + 1, right)
            
            return merge(left_side, right_side)
        
        merge_sort(nums, 0, len(nums) - 1)
        return self.counts
            
