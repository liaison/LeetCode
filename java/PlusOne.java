import java.util.Arrays;


/**
 * 
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

 * @author Lisong Guo <lisong.guo@me.com>
 * @date   22 Dec, 2014
 *
 */
public class PlusOne {

	/**
    public int[] plusOne(int[] digits) {
    	int size = digits.length;
    	int carry = 1;
    	int [] res = new int[size];
    	
    	for(int i=size-1; i>=0; i--){
    		int sum = (digits[i] + carry);
    		carry =  sum / 10;
    		res[i] = sum % 10;
    	}
    	
    	if(carry == 0){
    		return res;
    	}else{
    		// This is less likely to happen, therefore, good for the performance. 
    		int [] newRes = new int[size+1];
    		for(int i=1; i<size+1; i++){
    			newRes[i] = res[i-1];
    		}
    		newRes[0] = 1;
    		return newRes;
    	}
    }
    */
	
	/**
	 * A solution inspired by the code handbook.
	 */
    public int[] plusOne(int[] digits) {
    	int size = digits.length;
    	int i = size;
    	
    	while(--i >= 0) {
    		// Find the fist non-9 digit
    		if(digits[i] < 9){
    			digits[i] ++;
    			return digits;
    		}else{
    			digits[i] = 0;
    		}
    	}
    	
		// all digits are 9, otherwise return in above cycle
		int[] newRes = new int[size + 1];
		Arrays.fill(newRes, 0);
		newRes[0] = 1;
		return newRes;
	}
    
	public static void main(String[] args) {
		//int [] digits = {9, 1, 9}; // expected 920
		int [] digits = {9, 1, 9}; // expected 1000
		
		PlusOne solution = new PlusOne();
		Utils.printArray(solution.plusOne(digits));
	}

}
