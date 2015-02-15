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
import java.util.ArrayList;

public class GreyCode {
	
	/**
	 * 
     * https://oj.leetcode.com/discuss/25375/recursive-solution-c-6-ms-with-explaination
	 * The sequence of grey code is symmetric.
	 */
    public List<Integer> grayCode(int n) {
    	List<Integer> res = new ArrayList<Integer>();
    	if(n == 0) {
    		res.add(0); // expected by the online judge, instead of an empty list.
    		return res;
    	}
    	
    	// n = 1, bottom case / starting point.
    	res.add(0);
    	res.add(1);
    	
    	int shift = 1;
    	while(shift < n) {
    		int size = res.size();
    		// Create symmetric codes of the current grey code, except the highly bit.
    		for(int j=size-1; j>=0; --j) {
    			int newCode = res.get(j) | (1 << shift); 
    			res.add(newCode);
    		}
    		
    		++shift;
    	}
    	
    	return res;
    }

	public static void main(String[] args) {
		
		GreyCode solution = new GreyCode();
		Utils.printList(solution.grayCode(4));
		// n = 2, expected:  0,1,3,2,6,7,5,4
		// n = 3, expected:  0,1,3,2,6,7,5,4,12,13,15,14,10,11,9,8
		// n = 4, expected: 
	}

}





