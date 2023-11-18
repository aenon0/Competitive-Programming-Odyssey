class Solution {
public:
    int maxSumTwoNoOverlap(vector<int>& nums, int firstLen, int secondLen) {
        if (nums.size()<firstLen + secondLen){
            return 0;
        }
        vector <int> pre_sum=nums;
        for (int i=1; i<nums.size();i++){
            pre_sum[i]+=pre_sum[i-1];
        }
        int res=pre_sum[firstLen+secondLen-1],max_L=pre_sum[firstLen-1],max_M=pre_sum[secondLen-1];
        for (int i=firstLen+secondLen; i<nums.size();i++){
            max_L =max(max_L, pre_sum[i-secondLen]-pre_sum[i-firstLen-secondLen]);
            max_M =max(max_M, pre_sum[i-firstLen]-pre_sum[i-firstLen-secondLen]);
            res=max(res,max(max_L+ pre_sum[i]-pre_sum[i-secondLen], max_M+ pre_sum[i]-pre_sum[i-firstLen]));
            
        }
        return res;
    }
};
