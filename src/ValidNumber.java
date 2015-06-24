/**

Validate if a given string is numeric.

Some examples:

"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. 
You should gather all requirements up front before implementing one.

 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Dec 30, 2014
 *
 */
public class ValidNumber {

	
    public boolean isNumber(String s) {
    	int i = 0, n=s.length();
    	boolean isNumeric=false;
    	
    	if(n>0 && s.charAt(n-1) == 'e'){
    		// "0.e"
    		return false;
    	}
    	
    	// ignore the leading space
    	while(i<n && s.charAt(i) == ' ') ++i;
    	
    	// ignore the sign
    	if(i<n && (s.charAt(i) == '-' || s.charAt(i) == '+')) ++i;
    	
    	// scan the first digital part.
    	while(i<n && Character.isDigit(s.charAt(i))){
    		isNumeric = true;
    		++i;
    	}
    	
    	boolean isDot = false;
    	// scan the second part digital part
    	if(i<n){
    		
    		if(s.charAt(i) == '.'){
    			
        		if(0<i && Character.isDigit(s.charAt(i-1))){
        			isNumeric = true;
        			if(i<n-1 && s.charAt(i+1) == 'e'){
        				++i;
        			}
        		}else{
        			isDot = true;
        		}
    		}
    		
    		if(0<i && Character.isDigit(s.charAt(i-1)) && s.charAt(i) == 'e'){
    			isNumeric = false;
    		}
    		
    		if(isDot){
    			++i;
    			while(i<n && Character.isDigit(s.charAt(i))){
    				++i;
    			}
    		}
    		
    		++i;
    		
    		while(i<n && Character.isDigit(s.charAt(i))){
    			isNumeric = true;
    			++i;
    		}
    	}
    	
    	// trailing spaces
    	while(i<n && s.charAt(i) == ' ') ++i;
    	
    	return isNumeric && i==n;
    }
	
	public static void main(String[] args) {
		//String s = " 2e10";
		//String s = "0.1";
		//String s = ".1"; // true
		//String s = "e2"; // false
		//String s = "3.";   // true;
		//String s = ".";  // false;
		//String s = " ."; // false;
		//String s = " e0"; // false;
		String s = "46.e3";  // true;
		//String s = "0.e";   // false;
		//String s = ".2e81";  // true;
		
		ValidNumber solution = new ValidNumber();
		
		System.out.println(solution.isNumber(s));
	}

}
