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

    public int[] plusOne(int[] digits) {
    	int size = digits.length;
    	int carry = 1;
    	int [] res = new int[size+1];
    	
    	for(int i=size-1; i>=0; i--){
    		int sum = (digits[i] + carry);
    		carry =  sum / 10;
    		res[i+1] = sum % 10;
    	}
    	
    	if(carry == 1){
    		res[0] = 1;
    		return res;
    	}else{
    		return Arrays.copyOfRange(res, 1, size+1);
    	}
    }
    
    
	public static void main(String[] args) {
		int [] digits = {1, 2, 9};
		
		PlusOne solution = new PlusOne();
		Utils.printArray(solution.plusOne(digits));
	}

}
