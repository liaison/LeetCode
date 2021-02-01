import java.util.Arrays;

/**

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order 
(ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and 
its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

 * @author Lisong Guo <lisong.guo@inria.fr>
 * @date   Nov 11, 2014
 */

public class NextPermutation {

    // This is actually the selection sort, NOT bubble sort.
	// Each outer round, the number for the position [i] would be determined. 
	private static void selectionSort(int [] num, int start){
		for(int i=start; i<num.length; i++){
			for(int j=i; j<num.length; j++){
				if(num[i] > num[j]){
					int temp = num[i];
					num[i] = num[j];
					num[j] = temp;
				}
			}
		}
	}
	
	private static void bubbleSort(int [] num, int start){
		int count = num.length - start + 1;
		
		for(int i=0; i<count; ++i){
			// for each iteration, the biggest element sinks to the bottom.
			for(int j=start; j<num.length-i-1; ++j){
				if(num[j] > num[j+1]){
					int temp = num[j];
					num[j] = num[j+1];
					num[j+1] = temp;
				}
			}
		}
	}
	
    public void nextPermutation(int[] num) {

		int w = num.length - 1;
		int max_i = -1, i_w = -1;
		
		while (w > 0) {
			for (int i = w - 1; i >= 0; i--) {
				if (num[w] > num[i]) {
					if(i > max_i){
						max_i = i;
						i_w = w;
					}
				}
			}
			w--;
		}
		
		if(max_i != -1){
			// Find the best switching point.
			int temp = num[max_i];
			num[max_i] = num[i_w];
			num[i_w] = temp;

			// Do the bubble sort to get the minimal number.
			bubbleSort(num, max_i+1);

		}else{
			// Did not find any solution
			Arrays.sort(num);
		}
    }

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		//int[] A = {1, 2, 3};	// expected result: {1, 3, 2}
		//int[] A = {3, 2, 1};	// expected result: {1, 2, 3}
		//int[] A = {1, 1, 5};  	// expected result: {1, 5, 1}
		
		//int [] A = {1, 2}; 		// expected answer {2, 1};
		int [] A = {2, 3, 1};  	// expected {3, 1, 2};
		
		//int [] A = {4,2,0,2,3,2,0}; // expected result: {4,2,0,3,0,2,2}

		Utils.printArray(A);
		
		NextPermutation solution = new NextPermutation();
		
		solution.nextPermutation(A);
		
		Utils.printArray(A);
	}

}






