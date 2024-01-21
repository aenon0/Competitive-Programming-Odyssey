class Solution {
  int rob(List<int> nums) {
      if (nums.length == 1){
          return nums[0];
      }
      for (int i = 2; i < nums.length; i++){
          int temp = nums[i - 2];
          if ((i - 3) > -1 && nums[i - 3] > temp){
              temp = nums[i - 3];
          }
          nums[i] += temp;
              
      }
      print(nums);
      return max(nums[nums.length - 1], nums[nums.length - 2]);
        
      
  }
}