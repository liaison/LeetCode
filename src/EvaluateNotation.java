import java.util.Stack;


/**
 
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
  
 * @author Lisong Guo <lisong.guo@inria.fr>
 * @date   28 Nov, 2014
 */

public class EvaluateNotation {

	
    public int evalRPN(String[] tokens) {
        
    	Stack<String> eval = new Stack<String>();
    	
    	for(String token : tokens){
    		if( token.equals("+") || token.equals("-") ||
    			token.equals("*") || token.equals("/")){
    			
    			int opr_1 = Integer.valueOf(eval.pop());
    			int opr_2 = Integer.valueOf(eval.pop());
    		
    			if(token.equals("+")){
    				eval.push(String.valueOf(opr_1 + opr_2));
    			}else if(token.equals("-")){
    				eval.push(String.valueOf(opr_2 - opr_1));
    			}else if(token.equals("*")){
    				eval.push(String.valueOf(opr_1 * opr_2));
    			}else if(token.equals("/")){
    				eval.push(String.valueOf(opr_2 / opr_1));
    			}
    		}else{
    			eval.push(token);
    		}
    	}
    	
    	return Integer.valueOf(eval.pop());
    }
    
    
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String [] tokens = {"2", "1", "+", "3", "*"};
		EvaluateNotation solution = new EvaluateNotation();
		
		System.out.println(solution.evalRPN(tokens));
	}

}
