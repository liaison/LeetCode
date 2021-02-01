import java.util.Arrays;
import java.util.Stack;


/**
 * 
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Jan 06, 2015
 *
 */
public class Histogram {

	/**
    public int largestRectangleArea(int[] height) {
        int max_area = 0;
        int next_iter = 0;
        int iter = 0;
    	while(iter < height.length){
    		int len = height[iter];
    		
    		int j=iter;
    		while(j<height.length && height[j] == len){
    			++j;
    		}
    		next_iter = j; // skip the flat region in between.
    		max_area = Math.max(max_area, len*(j-iter));
    		
    		for(j=iter; j<height.length && len > 0; ++j){
    			len = Math.min(len, height[j]);
    			max_area = Math.max(max_area, len*(j-iter+1));
    		}
    		
    		iter = next_iter;
    	}
    	
    	return max_area;
    }
    */
    
	/**
	public int largestRectangleArea(int[] height) {
        int max_area = 0;
        
    	for(int i=0; i<height.length; ++i){
    		int len = height[i];
    		for(int j=i; j<height.length && len > 0; ++j){
    			len = Math.min(len, height[j]);
    			max_area = Math.max(max_area, len*(j-i+1));
    		}
    	}
    	
    	return max_area;
    }
    */
    
    
	/**
	 * https://oj.leetcode.com/discuss/12780/my-concise-c-solution-ac-90-ms
	 */
    public int largestRectangleArea(int[] height) {
    	
    	Stack<Integer> stack = new Stack<Integer>();
    	int max_area = 0;
    	
    	for(int i=0; i<=height.length; ++i){
    		int height_bound = (i == height.length) ? 0 : height[i];
    		
    		while(!stack.isEmpty()){
    			int h = height[stack.peek()];
    			
    			// calculate the area for every ascending slope.
    			if(h < height_bound){
    				break;
    			}
    			stack.pop();
    			
    			// at the end, the area with the height of the minimal element.
    			int index_bound = stack.isEmpty() ? -1 : stack.peek();
    			max_area = Math.max(max_area, h*((i-1)-index_bound));
    		}
    		
    		stack.push(i);
    	}
    	
    	return max_area;
	}

	
	public static void main(String[] args) {
		//int [] height = {2,1,5,6,2,3};  // expect 10
		//int [] height = {2,3,5,6};  // expect 10
		//int [] height = {1, 1, 1, 1, 1};  // expect 10
		
		
		int [] height = new int [2000000];
		Arrays.fill(height, 1);
		
		long time = System.currentTimeMillis();
		
		Histogram solution = new Histogram();
		System.out.println(solution.largestRectangleArea(height));
	
		System.out.println(System.currentTimeMillis() - time);
		
	}

}
