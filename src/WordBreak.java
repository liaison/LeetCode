import java.util.HashSet;
import java.util.Set;

/**
 * 
 * @author Lisong Guo <lisong.guo@inria.fr> 
 * @date   27 Nov, 2014
 *

Given a string s and a dictionary of words dict, 
 determine if s can be segmented into a space-separated 
 sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

 *
 */

public class WordBreak {

	/**
	 * a recursive solution
	 * 
	 * @param s
	 * @param dict
	 * @return
	 */
    public boolean wordBreak(String s, Set<String> dict) {
    	
    	// early exits
    	if(s == null || s.length() == 0) return false;
    	if(dict.contains(s))	return true;
    	
    	boolean earlyStop = true;
    	for(int i=s.length()-1; i>0; i--){
    		if(dict.contains(s.substring(i))){
    			earlyStop = false;
    			break;
    		}
    	}
    	// No need to do the recursion.
    	if(earlyStop){
    		return false;
    	}
    	
		// find matches for the substrings of s,
		// starting from long substring to short ones
		for (int i = s.length()-1; i > 0; i--) {
			String slide = s.substring(0, i);
			if (dict.contains(slide)) {

				if (wordBreak(s.substring(i), dict)) {
					return true;
				}
			}
		}
		
		return false;
	}
    
    /**
     * a DP solution 
     * @param s
     * @param dict
     * @return
     */
    public boolean wordBreak_dp(String s, Set<String> dict) {
    	
    	for(int i=s.length()-1; i>0; i--){
    		String slide = s.substring(i);
    		
    		if(dict.contains(slide)){
    			
    		}
    	}
    	
    	return true;
    }
    
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		HashSet<String> dict = new HashSet<String>();
		
		/*
		dict.add("leet");
		dict.add("code");
		String s = "leetcode";
		*/
		
		/* "bb", ["a","b","bbb","bbbb"], expected true
		// "aaaaaaa", ["aaaa","aaa"]     expected true
		dict.add("aaaa");
		dict.add("aaa");
		String s = "aaaaaaa";
		*/
		
		// "abcd", ["a","abc","b","cd"]  expected true
		dict.add("a");
		dict.add("abc");
		dict.add("b");
		dict.add("cd");
		String s = "abcd";
		
		WordBreak solution = new WordBreak();
		
		System.out.println(solution.wordBreak(s, dict));
	}

}























