/**
 * The gray code is a binary numeral system 
 * 	where two successive values differ in only one bit.

	Given a non-negative integer n representing the total number of bits in the code, 
		print the sequence of gray code. A gray code sequence must begin with 0.

	For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

		00 - 0
		01 - 1
		11 - 3
		10 - 2
	Note:
		For a given n, a gray code sequence is not uniquely defined.

	For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

	For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Feb 14, 2015
 *
 */
import java.util.List;
import java.util.LinkedList;

public class GreyCode {
	
    public List<Integer> grayCode(int n) {
    	List<Integer> res = new LinkedList<Integer>();
   
    	if(n == 0) {
    		res.add(0);
    		return res;
    	} else if(n == 1) {
    		res.add(0);
    		res.add(1);
    		return res;
    	} else if(n == 2) {
    		res.add(0);
    		res.add(1);
    		res.add(3);
    		res.add(2);
    		return res;
    	}
    	
    	int size = 1 << (n-2);
    	int [] index = {0, 1, 3, 2, 2, 3, 1, 0};
    	int count = 0;
    	
    	int base_i = 0;
    	int offset_i = 0;
    	
    	while(count < size) {
    		
    		for(int i=0; i<4; ++i) {
    			res.add(4 * index[base_i] + index[offset_i] + (count < 4 ? 0 : count/4) * 16);
        		offset_i = (offset_i+1) % 8;
    		}
    		
    		base_i = (base_i+1) % 8;
    		
    		++ count;
    	}
    	
    	return res;
    }

	public static void main(String[] args) {
		
		GreyCode solution = new GreyCode();
		Utils.printList(solution.grayCode(6));
		// n = 2, expected:  0,1,3,2,6,7,5,4
		// n = 3, expected:  0,1,3,2,6,7,5,4,12,13,15,14,10,11,9,8
		// n = 4, expected: 
	}

}





