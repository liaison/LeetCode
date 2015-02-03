/**
 * 
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Feb 3, 2015
 * 
 * Given n pairs of parentheses, write a function to generate 
 * 		all combinations of well-formed parentheses.

	For example, given n = 3, a solution set is:
		"((()))", "(()())", "(())()", "()(())", "()()()"
 */

import java.util.LinkedList;
import java.util.List;

public class GenerateParenthese {
	
	/**
	 * The recursive solution is based on the following formulas: 

		F(n) = “(“ + F(i) + “)” + F(n-i-1) 

		where F(n) is the desired function that 
			returns a list of combination with the specified number of parenthesis. 

		The formula says that the result can be obtained by the “divide-and-conquer” principle, 
			in this case, the combinations can be obtained by dividing the string into two parts, 
			the left part would be embraced by a pair of parenthesis, 
			and then appended with the right right without parenthesis, 
			we get a combination. 
	 */
    public List<String> generateParenthesis(int n) {
    	LinkedList<String> res = new LinkedList<String>();
		
		if (n == 0){
			res.add("");
			return res;
		} else if (n == 1){
			res.add("()");
			return res;
		}
		
        for(int i=n-1; i>=0; --i){
        	List<String> l = generateParenthesis(i);
        	List<String> r = generateParenthesis(n-i-1);
        	
        	for(String l_str : l){
        		for(String r_str : r){
            		res.add("(" + l_str + ")" + r_str);
        		}
        	}
        }
        
        return res;
    }
    
	public static void main(String[] args) {
		GenerateParenthese solution = new GenerateParenthese();
		List<String> res = solution.generateParenthesis(3);
		
		Utils.printStringList(res);
	}

}
