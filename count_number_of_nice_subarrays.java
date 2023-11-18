class Solution {
    public int numberOfSubarrays(int[] nums, int k) {
        int n=nums.length, ans=0;
        int[] pre=new int[n+1];
        pre[0]=0;
        int [] cnt =new int[n+1];
        Arrays.fill(cnt,0);
        cnt[0]=1;
        for(int i=0; i<n; i++){
            pre[i+1]=pre[i]+ (nums[i] & 1);
            if(pre[i+1]>=k){
                ans+=cnt[pre[i+1]-k];
            }
            cnt[pre[i+1]]+=1;
        }
        return ans;        
    }
}
