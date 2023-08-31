class Solution {
public:
    int findNumbers(vector<int>& nums) {
      int ans=0,n=nums.size();
        for(int i=0;i<n;i++)
        {
            //find the number of digits
            int hi=log10(nums[i])+1;
            if(hi%2==0)ans++;
        
        }
        return ans;
    }
};   