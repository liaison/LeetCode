
/**
 * 
 * Given an integer n, return the number of trailing zeroes in n!.
 * 
 * Note: Your solution should be in logarithmic time complexity.
 * 
 * @author Lisong Guo <lisong.guo@.me.com>
 * @date   Jan 13, 2015
 *
 */
public class FactorialTrailingZeros {

	
    public int trailingZeroes_p(int n) {
    	//  1, 2, 3, 4, 5, 6, 7, 8, 9. 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
    	
    	long fn = 1; 
    	int c = n;
    	
    	while(c > 1){
    		fn = fn * c;
    		c--;
    	}
    	
    	System.out.println(fn);
    	
    	c = 0;
    	while(fn > 9 && fn % 10 == 0){
    		fn = fn / 10;
    		c++;
    	}
    	
    	return c;
    }
    
	
    /**
     * https://oj.leetcode.com/discuss/20691/my-explanation-of-the-log-n-solution
     */
	public int trailingZeroes(int n) {
		int power = 1;
		int c = 0;
		int f = (int) (n/(Math.pow(5, power)));
		
		while(f > 0){
			c += f;
			f = (int) (n/(Math.pow(5, ++power)));
		}
		
		return c;
	}
	
	public static void main(String[] args) {
		int n = 10;
		//int n = 2147483647;
		
		FactorialTrailingZeros solution = new FactorialTrailingZeros();
		System.out.println(solution.trailingZeroes(n));
		
		System.out.println(solution.trailingZeroes_p(n));
		
	}
}





