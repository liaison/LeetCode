/**

A peak element is an element that is greater than its neighbors.
Given an input array where num[i] ≠ num[i+1], 
	find a peak element and return its index.
The array may contain multiple peaks, 
	in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element 
	and your function should return the index number 2.

Note:
	Your solution should be in logarithmic complexity.

 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Jan 15, 2015
 *
 */
public class FindPeakElement {

    public int findPeakElement(int[] num) {
    	int low=0, high=num.length, mid = 0;
    	
    	while(low < high){
    		 mid = (low+high)/2;
    		
    		if(num[mid] > num[mid-1]){
    			
    		}
    	}
    	
    	return mid;
    }
    
    public static void main(String[] args) {
    	
	}

}
