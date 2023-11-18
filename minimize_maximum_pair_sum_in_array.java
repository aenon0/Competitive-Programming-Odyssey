class Solution {
    public int minPairSum(int[] nums) {
        Arrays.sort(nums);
        int sum=0,max=0;
        int i=0;
        int j=nums.length-1;
        while (i<nums.length/2 && j>=nums.length/2){
            
          
                sum=nums[i]+nums[j];
                max=Math.max(sum,max);
                sum=0;
            i++;
            j--;
        }
        return max;
        
    }
}
