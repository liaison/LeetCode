import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;


/**
 * Radix sort algorithm
 * 	  "non-comparative" sorting algorithm, there is no comparison between the elements to sort. 
 * 
 * The complexity of the algorithm is O(bN), where b depends on the maximum element, 
 * 	up to the maximal value for the data type of all elements.
 *  
 * @author Lison Guo <lisong.guo@me.com>
 * @date   Jan 03, 2015
 *
 */
public class RadixSort {

	public void radixSort(int [] num){

		int max = Integer.MIN_VALUE;
		// Initialise the memory buffer for the radix sorting.
		ArrayList<Integer> sortBuffer = new ArrayList<Integer>();
		for(int n : num){
			max = n > max ? n : max;
			sortBuffer.add(n);
		}
		
		int mask = 2;
		int bit_num = 1; // the number of bits for the max value.
		while(max / mask > 0){
			++bit_num;
			mask <<= 1;
		}
		
		ArrayList<Integer> bucket0 = new ArrayList<Integer>();
		ArrayList<Integer> bucket1 = new ArrayList<Integer>();
		
		mask = 1;
		// Do the radix sort up to the "bit_num" round, instead of 32.
		while(bit_num-- > 0){
			
			for(Integer n : sortBuffer){
				boolean eb = ((int)n & mask) == 0 ? 
					bucket0.add(n) : bucket1.add(n);
			}
			mask <<= 1;
				
			sortBuffer.clear();
			sortBuffer.addAll(bucket0);
			sortBuffer.addAll(bucket1);
			
			bucket0.clear();
			bucket1.clear();
			
		}
		
		// Copy the sorted list to the original list.
		for(int i=0; i<num.length; ++i){
			num[i] = sortBuffer.get(i);
		}
	}
	
	
	public int maximumGap(int[] num) {
		if(num.length < 2){
			return 0;
		}
		
		this.radixSort(num);
		int max_gap = Integer.MIN_VALUE;
		
		for(int i=1; i<num.length; i++){
			int gap = num[i]-num[i-1];
			max_gap = gap > max_gap ? gap : max_gap; 
		}
		return max_gap;
	}
	

	public static void main(String[] args) {
		//int [] num = {4, 5, 3, 9}; // expect 4
		//int [] num = {2, 3};    // expect 1
		//int [] num = {};        // expect 0;
		//int [] num = {3,6,9,1}; // expect 3
		int [] num = {100,3,2,1};  // expect 97
		
		RadixSort solution = new RadixSort();
		
		solution.radixSort(num);
		Utils.printArray(num);
		
		//System.out.println(solution.maximumGap(num));
	
	}

}
