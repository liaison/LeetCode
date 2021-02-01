
/**
 * 
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Mar 15, 2015
 */
public class HammingWeight {

	// you need to treat n as an unsigned value
    public int hammingWeight(int n) {
    	int c = 0; 
    	int mask = 1;
    	
    	while (n != 0) {
    		if ((n & mask) == 1) {
    			++c;
    		}
    		//Should use the logical shift >>>, 
    		//  instead of arithmetic shift >>, which puts 1 for left most bit,
    		//  if the number is negative. 
    		n >>>= 1;
    	}
    	
    	return c;
    }
	
	public static void main(String[] args) {
		//int n = 2147483648;
		int n = 1;
		HammingWeight hw = new HammingWeight();
		
		System.out.println(hw.hammingWeight(n));
	}

}
