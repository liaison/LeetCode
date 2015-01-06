
/**
 * 
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Jan 06, 2015
 *
 */
public class Histogram {

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
	
	public static void main(String[] args) {
		int [] height = {2,1,5,6,2,3};
	
		Histogram solution = new Histogram();
		System.out.println(solution.largestRectangleArea(height));
	}

}
