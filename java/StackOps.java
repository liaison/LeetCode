import java.util.HashMap;
import java.util.Stack;


/**
 * 
 * A list of problems that can be solved with the stack data structure. 
 * 
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Dec 10, 2014
 *
 */
public class StackOps {

	/**
	 *  Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
	 * 	determine if the input string is valid.

		The brackets must close in the correct order, 
			"()" and "()[]{}" are all valid but "(]" and "([)]" are not.
	 * @param s
	 * @return
	 */
    public boolean isValid(String s) {
    	Stack<Character> parenStack = new Stack<Character>();
    	HashMap<Character, Character> parenPair = 
    			new HashMap<Character, Character>();
        parenPair.put(')', '(');
        parenPair.put(']', '[');
        parenPair.put('}', '{');
        
    	for(int i=0; i<s.length(); i++){
        	char c = s.charAt(i);
        	switch(c){
        		case '(':
        		case '[':
        		case '{':
        			parenStack.push(c);
        			break;
        		case ')':
            	case ']':
            	case '}':
        			if(parenStack.isEmpty()){
        				return false;
        			}else if(parenStack.peek().equals(parenPair.get(c))){
            			parenStack.pop();
            		}else{
            			return false;
            		}
        			break;
        		default:
        			break;
        	}
        }
    	
    	return parenStack.isEmpty();
    }
    
	public static void main(String[] args) {
		//String input = "(){}";
		String input = ")";
		
		StackOps solution = new StackOps();
		
		System.out.println(solution.isValid(input));
	}

}









