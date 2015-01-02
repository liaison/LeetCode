import java.util.Arrays;

/**
 * 
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Jan 02, 2014
 *
 */
public class MaximumGap {

	
    public int maximumGap(int[] num) {
    	if(num.length < 2){
    		return 0;
    	}
    	
    	Arrays.sort(num);
    	
    	int max_gap = Integer.MIN_VALUE;
    	for(int i=1; i<num.length; i++){
    		int gap = num[i] - num[i-1];
    		max_gap = gap > max_gap ? gap : max_gap;
    	}
    	
    	return max_gap;
    }
    
    
	public static void main(String[] args) {
		int [] num = {1, 4, 5, 3};
		
		MaximumGap solution = new MaximumGap();
		System.out.println(solution.maximumGap(num));
		
	}

}



