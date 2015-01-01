
/**
 * 
 * Write a function to find the longest common prefix string amongst an array of strings.
 * 
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Jan 1, 2015
 *
 */
public class LongestCommonPrefix {

    public String longestCommonPrefix(String[] strs) {
    	if(strs == null || strs.length == 0){
    		return "";
    	}
    	
    	boolean isFound = false;
    	int pc = 0;
    	while(! isFound){
    		
    		int c = -1;
    		int i = 0;
    		
    		for(; i<strs.length; ++i){
    			
    			if(pc >= strs[i].length()){
        			isFound = true;
    				break;
        		}
        		
    			if(c == -1){
    				c = strs[i].charAt(pc);	
    			}
    			
    			if(c != strs[i].charAt(pc)){
    				isFound = true;
    				break;
    			}
    		}
    		
    		++pc;
    	}
    	
    	return strs[0].substring(0, pc-1);
    }
    
    public static void main(String[] args) {
    	//String [] strs = {"ABC", "A", "ABC"};
    	String [] strs = {};
    	
    	LongestCommonPrefix solution = new LongestCommonPrefix();
    	System.out.println(solution.longestCommonPrefix(strs));
	}

}






