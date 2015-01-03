
/**
 * A bucket sort algorithm to solve the maximum gap problem in linear time and space.
 * 
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Jan 02, 2015
 *
 */
public class BucketSort {


    public int maximumGap(int[] num) {
    	if(num.length < 2){
    		return 0;
    	}
    	
    	// Find the min and max elements in the list.
    	int min = Integer.MAX_VALUE;
    	int max = Integer.MIN_VALUE;
    	for(int e : num){
    		min = Math.min(e, min);
    		max = Math.max(e, max);
    	}
      	
    	// Put the n elements into (n-1) buckets. 
    	double div = (max-min)*1.0/(num.length-1);
    	
    	// bucket[i]  : min value in the bucket i/2;
    	// bucket[i+1]: max value in the bucket i/2;
    	// Note: the elements are all non-negatives.
    	int [] bucket = new int[num.length*2];
    	for(int e : num){
    		int i = (int)((e-min)/div) * 2;
    		
    		bucket[i]   = bucket[i] == 0 ? e : Math.min(e, bucket[i]);
    		bucket[i+1] = bucket[i+1] == 0 ? e : Math.max(e, bucket[i+1]);
    	}
    	
    	// Calculate the maximum distance between buckets, 
    	//  which is aslo the maximum gap between elements.
    	int last_bound = min;
    	int max_gap = Integer.MIN_VALUE;
    	for(int i=0; i<num.length*2; i+=2){
    		if(bucket[i] == 0){
    			// no element in this bucket.
    			continue;
    		}
    		
    		max_gap = Math.max(bucket[i]-last_bound, max_gap);
    		last_bound = bucket[i+1];
    	}
    	
    	return max_gap;
    }
    
    
	public static void main(String[] args) {
		int [] num = {4, 5, 3, 9};
		//int [] num = {2, 3};
		//int [] num = {3,6,9,1}; // expect 3
		
		BucketSort solution = new BucketSort();
		System.out.println(solution.maximumGap(num));
	
	}

}
