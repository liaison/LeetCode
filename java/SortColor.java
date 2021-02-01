
/**
 * 
 * 
 * Given an array with n objects colored red, white or blue, 
 * sort them so that objects of the same color are adjacent, 
 * with the colors in the order red, white and blue.

	Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

	Note:
		You are not suppose to use the library's sort function for this problem.

	Follow up:
		A rather straight forward solution is a two-pass algorithm using counting sort.
		First, iterate the array counting number of 0's, 1's, and 2's, 
		then overwrite array with total number of 0's, then 1's and followed by 2's.

		Could you come up with an one-pass algorithm using only constant space?

 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Jan 04, 2015
 *
 */
public class SortColor {

	/**
	 * Divide the array into three partition, two pointers pointed to the head and tail, 
	 * 	move the smallest to the head and the largest to the tail, at the end, 
	 * 	we would have the medium in the middle. 
	 * @param A
	 */
    public void sortColors(int[] A) {
        int hd = 0, tl = A.length-1;
        int cur = 0;
        while(cur <= tl){
        	switch(A[cur]){
        	case 0:
        		A[cur++] = A[hd];
        		A[hd++] = 0;
        		break;
        	case 1:
        		cur++;
        		break;
        	case 2:
        		A[cur] = A[tl];
        		A[tl--] = 2;
        		break;
        	}
        }
    }
    
    
	public static void main(String[] args) {
		//int [] A = {1, 0, 0, 2, 0, 1};
		//int [] A = {1, 2, 0};
		int [] A = {2, 1};  // output: {1, 2};
		
		SortColor solution = new SortColor();
		solution.sortColors(A);
		Utils.printArray(A);
	}

}
