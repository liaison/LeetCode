/**

Given a sorted array of integers, 
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
	Given [5, 7, 7, 8, 8, 10] and target value 8,
	
	return [3, 4].

 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Feb 23, 2015
 *
 */
public class SearchRange {

    public int[] searchRange(int[] A, int target) {
        int low=0, mid = 0, high=A.length-1;
        
        while (low <= high) {
        	mid = (high+low)/2;
        	if (A[mid] == target) {
        		break;
        	} else if (A[mid] > target) {
        		high = mid-1;
        	} else {
        		low = mid + 1;
        	}
        }
        
        int [] res = new int[2];
        
        if (low > high) {
        	res[0] = res[1] = -1;
        	return res;
        } else {
        	res[0] = res[1] = mid;
        }
        
        while(res[0] >= 0 && A[res[0]] == target) res[0]--;
        while(res[1] < A.length && A[res[1]] == target) res[1]++;
        
        res[0] ++;
        res[1] --; 
        return res;
    }
    
    
    public static void main(String[] args) {
    	int [] A = {5, 7, 7, 8, 8, 10};
    	int target = 8;    // expected {3, 4}
    	
    	//int [] A = {1};
    	//int target = 0;      // expected {-1, -1}
    	
    	SearchRange solution = new SearchRange();
    	
    	Utils.printArray(solution.searchRange(A, target));
	}

}
