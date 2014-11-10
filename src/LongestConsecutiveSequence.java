import java.util.HashMap;


/**
 * 
 * 
 * Given an unsorted array of integers, 
 * find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

 * @author Lisong Guo <lisong.guo@inria.fr>
 * @date   Nov 09, 2014
 *
 */
public class LongestConsecutiveSequence {

	
	/**
	 * This solution exceeds the time limit. 
	 * 
	 */
	/*
	public int longestConsecutive(int[] num) {
		HashMap<Integer, Integer> num_table = new HashMap<Integer, Integer>();
		int max_count = Integer.MIN_VALUE; 
		
		for(int i=0; i<num.length; i++){
			
			num_table.put(num[i], 0);
			
			int count = 1;
			
			Integer l_neighbor = num[i]-1;		
			while(num_table.containsKey(l_neighbor)){
				count ++;
				l_neighbor -= 1;
			}
			
			Integer r_neighbor = num[i]+1;
			while(num_table.containsKey(r_neighbor)){
				count ++;
				r_neighbor += 1;
			}
			
			max_count = max_count > count ? max_count : count;
		}
		
		return max_count;
	}*/
	
	/**
	 * https://oj.leetcode.com/discuss/15117/accepted-short-solution-80-ms-scan-hash-map-with-explanation
	 * 
	 * 1. main idea is using hash map to check previous and next element in the sequence.
	 * 2. hash map holds length of consecutive sequence for start of sequence and end of sequence
	 * 3. we updating that values when joining intervals
	 * 4. longest sequence is calculated during joining intervals
	 * 
	 */
	public int longestConsecutive(int[] num) {
		int longest = 1;
		HashMap<Integer, Integer> num_table 
			= new HashMap<Integer, Integer>();
		
		for(int i=0; i<num.length; i++){
			int newItem = num[i];
			
			if(num_table.containsKey(newItem))
				continue;
			
			num_table.put(newItem, 1);
			
			Integer leftNeighbor = num_table.get(newItem-1);
			if(leftNeighbor != null){
				int newCount = leftNeighbor+1;
				num_table.put(newItem, newCount);
				num_table.put(newItem-newCount+1, newCount);
				longest = Math.max(newCount, longest);
			}
			
			Integer rightNeighbor = num_table.get(newItem+1);
			if(rightNeighbor != null){
				int newCount = num_table.get(newItem) + rightNeighbor;
				num_table.put(newItem - num_table.get(newItem) + 1 , newCount);
				num_table.put(newItem + rightNeighbor, newCount);
				longest = Math.max(newCount, longest);
			}
		}
		
		return longest;
	}

	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int [] num = {100, 4, 200, 1, 3, 2};
		LongestConsecutiveSequence solution 
			= new LongestConsecutiveSequence();
		
		System.out.println(solution.longestConsecutive(num));
	}

}



