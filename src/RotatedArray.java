
/**
 * https://oj.leetcode.com/problems/find-minimum-in-rotated-sorted-array/
 *

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
	or 5 6 7 0 1 2 4 
	
	
Find the minimum element.

You may assume no duplicate exists in the array.

 * @author Lisong Guo <lisong.guo@inria.fr>
 * @date   Nov 09, 2014
 *
 */

public class RotatedArray {

	/**
	 * Binary search 
	 * 
	 * Although this solution is recursive and more complicated than the following one, 
	 * 	it is faster!  
	 * 
	 *  384 ms vs. 440 ms. 
	 * 
	 * @param num
	 * @return
	 */
	
	/**
	public int findMin(int[] num) {
		int start = 0, end = num.length-1;
    	
		return findMin_rec(num, start, end);
	}
	
	public int findMin_rec(int[] num, int start, int end) {
    	
    	if(num.length == 1){
    		return num[0];
    	}
    	
    	int mid = 0;
    	while(start < end){
    		mid = (start+end)/2;
    		
    		if(mid==0){
    			return Math.min(num[0], num[1]);
    		}
    		
    		if(num[mid-1] < num[mid] && num[mid] > num[mid+1]){
    			return num[mid+1];
    		}else if(num[mid-1] > num[mid] && num[mid] < num[mid+1]){
    			return num[mid];
    		}else if(num[mid-1] < num[mid] && num[mid] < num[mid+1]){
    			return Math.min(findMin_rec(num, start, mid-1), 
    						    findMin_rec(num, mid+1, end));
    		}
    	}
    	
    	return num[start];
    }
    */
	
	/**
	 * https://oj.leetcode.com/discuss/14846/binary-search-solution-in-java
	 *  Compare the values of the start/end boundaries, instead its neighbour.
	 */
	public int findMin(int [] num){
		int l=0, h=num.length-1;
		if(num[l] < num[h]){
			// the array is NOT rotated.
			return num[l];
		}
		
		while(h-l > 1){
			int m = (l+h)/2;
			if(num[l] > num[m]){  // the rotation happens on the left side.
				h = m;
			}else{
				l = m;
			}
		}
		// reduce the search zone down to 2 elements at the end.
		return Math.min(num[l], num[h]);
	}
    
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int [] a = {6, 7, 0, 1, 2, 4, 5};
		//int [] a = {0, 1, 2, 4, 5, 6, 7};
		//int [] a = {2, 3, 4, 5, 1};
		
		//int [] a = {2, 1}; // expect 1; 
		
		RotatedArray solution = new RotatedArray();
		
		System.out.println(solution.findMin(a));
	}

	
	
}





