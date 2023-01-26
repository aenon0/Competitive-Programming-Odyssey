class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        so we got these two pointers one at the end of nums2 and another right before the non zero element of nums one
        if the number at ptrtwo is greater or equal to the num at ptrone then we put the number at ptrtwo at the end of nums1 
        else if the number at ptrtwo is less than the num at ptrone then we decrement ptrone by one
        """
        ptr= n+m-1
        ptr1=m-1
        ptr2=n-1
        while ptr2>=0:
            if nums1[ptr1] > nums2[ptr2] and ptr2>=0 and ptr1>=0:
                nums1[ptr]= nums1[ptr1]
                ptr-=1
                ptr1-=1
            else:
                nums1[ptr]= nums2[ptr2]
                ptr2-=1
                ptr-=1
               

            
            

        
