
class Solution {
    public void moveZeroes(int[] nums) {
        int n=nums.length, temp;
        for (int i=1; i<n; i++){
            for (int j=0; j<i; j++){
                
                if( (nums[j]==i-1 && nums[i]==0) || (j==i) ){
                    continue;
                }
                else if( nums[j]==0 ){
                    temp=nums[j];
                    nums[j]=nums[i];
                    nums[i]=temp;
                }
                
            }
        }  
        
       System.out.println(Arrays.toString(nums)); 
        
    }
};
