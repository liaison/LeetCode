/**

A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], 
find a peak element and return its index.

The array may contain multiple peaks, in that case return the index
to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

@author: Lisong Guo <lisong.guo@me.com
@date:   July 31, 2018

*/



#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        
        int low = 0, high = nums.size()-1;
        
        if(high == -1){
            // empty list
            return -1;
        }

        while(low < high){
            int mid = (low + high)/2;
            if(nums[mid] > nums[mid+1]){
                high = mid;
            } else {
                low = mid + 1;
            }
        }

        return low;
    }
};

int main(){
    Solution * s = new Solution();
    
    int a [] = {1,2,3,1};
    std::vector<int> nums (a, a+sizeof(a)/sizeof(*a));
    
    cout << s->findPeakElement(nums) << endl;

}

