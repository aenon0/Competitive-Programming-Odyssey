class Solution {
    public void sortColors(int[] nums) {
        int temp;
        for (int i=1; i<nums.length; i++){
            for (int j=1; j<nums.length; j++){
                if(nums[j-1]>nums[j]){
                    temp=nums[j];
               a     nums[j]=nums[j-1];
                    nums[j-1]=temp;
                }
            }
        }
    }
}
