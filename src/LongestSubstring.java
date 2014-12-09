import java.util.HashMap;
import java.util.HashSet;


/**
 * Given a string, find the length of the longest substring without repeating characters. 
 * 	For example, the longest substring without repeating letters for "abcabcbb" is "abc", 
 * 		which the length is 3. 
 * 	For "bbbbb" the longest substring is "b", with the length of 1.
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Dec 09, 2014
 *
 */
public class LongestSubstring {

	/**
    public int lengthOfLongestSubstring(String s) {
    	HashMap<String, Integer> dict = new HashMap<String, Integer>();
    	int end = s.length();
    	int max_size = Integer.MIN_VALUE;
    	
    	for(int i=0; i<end; i++){
    		dict.clear();
    		int count = 0;
    		for(int j=i; j<end; j++){
    			String k = String.valueOf(s.charAt(j));
    			if(dict.get(k) == null ){
    				dict.put(k, 1);
    			}else{
    				// find duplicate.
    				break;
    			}
    			count ++;
    		}
    		if(count > max_size){
    			max_size = count;
    		}
    	}
    	
    	return max_size;
    }
    */
	
	/**
	 * Dynamic programming
	 */
	public int lengthOfLongestSubstring(String s) {
		if(s == null || s.length() == 0){
			return 0;
		}
		int end = s.length();
    	int max_size = Integer.MIN_VALUE;
    	int pre_max_value = 0;
    	
		HashSet<String> dict = new HashSet<String>();
    	dict.add(String.valueOf(s.charAt(0)));
    	int count = 1;
    	
    	for(int j=1; j<end; j++){
    		String k = String.valueOf(s.charAt(j));
    		
    		if(dict.contains(k)){
    			break;
    		}else{
    			dict.add(k);
    			count ++;
    		}
		}
    	
    	pre_max_value = count;
    	max_size = pre_max_value;
		
    	if(max_size == end){
    		// early exit;
    		return max_size;
    	}
    	
    	for(int i=1; i < end; i++){
    		String preK = String.valueOf(s.charAt(i-1));
    		dict.remove(preK);
    		
    		count = pre_max_value - 1;
    		for(int j=i+count; j<end; j++){
    			String newK = String.valueOf(s.charAt(j));
        		
    			if(dict.contains(newK)){
        			break;
        		}else{
        			dict.add(newK);
        			count ++;
        		}	
    		}
    		
    		// prepare for the next one 
    		pre_max_value = count;
    		
    		if(count > max_size){
    			max_size = count;
    		}
    		
    		// early return;
    		if(pre_max_value + i == end){
    			break;
    		}
    		
    	}
    	
    	return max_size;
	}
    
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		//String s = "abcabcbb";
		String s = "bbbbb";
		LongestSubstring solution = new LongestSubstring();
		
		System.out.println(solution.lengthOfLongestSubstring(s));
	}

}









