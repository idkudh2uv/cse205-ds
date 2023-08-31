class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
 int count=0,i=0,j=1,n=arr.size();
        while(i<n&&count!=k){
            if(arr[i]==j){
                i++;
                j++;
            }
            else{
                j++;
                count++;
            }
            cout<<count<<endl;
        }
        j--;
        if(count!=k){
            j=k-count+arr[n-1];
        }
        return j;
    }
};