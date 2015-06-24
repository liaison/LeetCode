
/**
 * Integer operations 
 * 
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Dec 09, 2014
 *
 */
public class IntegerOps {
	
	/**
	 * 
	 * Reverse digits of an integer.

		Example1: x = 123, return 321
		Example2: x = -123, return -321
		
	 * @return
	 */
    public int reverse(int x) {
    	long newInt = 0;
    	
    	while(x != 0){
    		int digit = x % 10;
        	
    		if(newInt != 0){
    			newInt *= 10;
    			if(newInt > Integer.MAX_VALUE)
    				return 0; // overflow;
    			else if(newInt < Integer.MIN_VALUE)
    				return 0; // underflow;
    		}
    		
        	newInt += digit;
        	x = x / 10;
    	}
    	
    	return (int)newInt;
    }
    
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		//int x = 1534236469;  // overflow test case
		int x = -2147483648;   // underflow test case
		
		IntegerOps solution = new IntegerOps();
		
		System.out.println(solution.reverse(x));
	}

}
