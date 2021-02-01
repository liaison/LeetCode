
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
    	
    	int minLen = Integer.MAX_VALUE;
    	for(String str : strs){
    		minLen = Math.min(minLen, str.length());
    	}
    	
    	boolean isFound = false;
    	int pc = 0;
    	
    	while(! isFound && pc < minLen){
    		
    		int c = strs[0].charAt(pc);
    		
    		for(int i=1; i<strs.length; ++i){
    			
    			if(c != strs[i].charAt(pc)){
    				isFound = true;
    				break;
    			}
    		}
    		
    		++pc;
    	}
    	
    	return strs[0].substring(0, isFound ? pc-1 : pc);
    }
    
    public static void main(String[] args) {
    	//String [] strs = {"ABC", "ABCD", "ABC"};
    	String [] strs = {"a", "b"};
    	
    	//String [] strs = {};
    	
    	LongestCommonPrefix solution = new LongestCommonPrefix();
    	System.out.println(solution.longestCommonPrefix(strs));
	}

}






