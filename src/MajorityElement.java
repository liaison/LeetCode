
/**
 * 

Given an array of size n, find the majority element. 
The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Dec 24, 2014
 *
 */
public class MajorityElement {

	
    public int majorityElement(int[] num) {
    	if(num == null || num.length == 0)
    		return 0;
    	
    	int count = 1;
    	int iter = num[0];
    	int N = num.length;
    	
    	for(int i=1; i<N; i++){
    		if(num[i] != iter){
    			if(count == 0){
    				// new candidate
    				iter = num[i];
    				count = 1;
    			}else{
    				// count should be bigger than 0
    				count --;
    			}
    		}else{
    			count ++;
    		}
    		
    		if(count > N/2)
    			return iter; // early exit. Good for the performance.
    	}
    	
    	return iter;
    }
    
    
	public static void main(String[] args) {
		int [] num = {2, 2, 1, 1, 1, 1};
		
		MajorityElement solution = new MajorityElement();
		
		System.out.println(solution.majorityElement(num));
	}

}




