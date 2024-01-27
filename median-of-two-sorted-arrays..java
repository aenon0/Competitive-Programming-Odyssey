class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        double med=0,two=2; 
        
        int [] nums=new int[(nums1.length) + (nums2.length)];
        if(nums1.length>0){
            for (int i=0; i<nums1.length; i++){
                nums[i]=nums1[i];
            }
        }
        if(nums2.length>0){
            for (int i=0; i<nums2.length; i++){
                nums[nums1.length+i]=nums2[i];
            }
        }
        Arrays.sort(nums);
        if(nums.length%2==0 && nums.length!=0) {
            med=(nums[((nums.length)/2)-1]+nums[((nums.length)/2)])/two;
            
        }
        else if(nums.length%2!=0 && nums.length!=1 ){
            med=nums[(nums.length)/2 ];
        }
        else if(nums.length==1){
            med=nums[0];
        }
        else if(nums.length==0){
            med=0;
        }
        return med;
        
        
    }
}