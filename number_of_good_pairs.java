class Solution {
    public int numIdenticalPairs(int[] nums) {
        int i=0;
        int count=0;
        while (i<nums.length){
            
            for (int j=nums.length-1; j>i ;j--){
                if (nums[j]==nums[i]){
                    count++;
                }
            }
            
            i++;
        }
        return count;
    }
}
