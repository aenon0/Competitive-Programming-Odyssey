import java.util.*;
class Solution {
    public int maxArea(int[] height) {
        int right=(height.length)-1;
        int left=0;
        int maxArea=0;
        int currArea;
        
        while(left<right){
            
            currArea=(right-left)* (Math.min(height[left], height[right]));
            maxArea=Math.max(currArea, maxArea);
            
            if( height[left] < height[right] ){
                left++; 
            }  
            
            else if( height[left] >= height[right] ){
                right--; 
            }  
        }
    return maxArea;       
        
        
    }
}
