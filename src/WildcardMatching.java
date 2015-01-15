/**

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
	bool isMatch(const char *s, const char *p)

Some examples:
	isMatch("aa","a") → false
	isMatch("aa","aa") → true
	isMatch("aaa","aa") → false
	isMatch("aa", "*") → true
	isMatch("aa", "a*") → true
	isMatch("ab", "?*") → true
	isMatch("aab", "c*a*b") → false

	isMatch("aab", "*b") → true

	isMatch("aab", "*a*") → true


 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Jan 14, 2015
 *
 */
public class WildcardMatching {

	/** works, but TLE
    public boolean isMatch(String s, String p) {
    	int sl = s.length(), pl = p.length();
    	
    	if(sl == 0){
    		return pl == 0 || p.equals("*");
    	}
    	
    	int i = 0;
    	while(i < pl && i < sl){
    		
    		switch(p.charAt(i)){
    		
    			case '?':
    				return isMatch(s.substring(i+1), p.substring(i+1));
    			
    			case '*':
    				if(p.charAt(pl-1) != '*' && p.charAt(pl-1) != '?' &&
    						p.charAt(pl-1) != s.charAt(sl-1)){
    					return false;
    				}
    				
    				for(int j=i; j<=s.length(); ++j){
    					if(isMatch(s.substring(j), p.substring(i+1))){
    						return true;
    					}
    				}
    				// tried all possibility
    				return false;
 
    			default:
    				if(s.charAt(i) != p.charAt(i)){
    					return false;
    				}
    		}
    		
    		++i;
    	}
    	
    	return p.length() == s.length();
    }
    */
	
	/**
	 *https://oj.leetcode.com/discuss/20762/java-share-my-solution-with-comments
     */
    public boolean isMatch(String s, String p) {
        int ss=0,pp=0;
        int marked = -1;
        String p2 = p+'^'; // In case that the last char in p is *

        while(ss<s.length() && pp<p2.length()){
            if(s.charAt(ss) == p2.charAt(pp) || p2.charAt(pp)=='?'){
                ss++;
                pp++;
            }
            else if(p2.charAt(pp)=='*'){
                pp++;
                marked = pp;
            }
            else{
                if(pp==marked){
                    ss++;
                }
                else{
                    if(marked!=-1){ 
                        ss = ss - (pp - marked - 1);
                        pp = marked;
                    }
                    else return false;
                }
            }
        }

        while(pp<p.length()){
            if(p.charAt(pp)!='*'){
                return false;
            }
            pp++;
        }
        return ss>=s.length();
    }
    
    public static void main(String[] args) {
    	//String s = "aab", p = "*b";  // expected true
    	//String s = "aa", p = "a";    // expected false
    	//String s = "aa", p = "aa";   // expected true
    	
    	//String s = "aaa", p = "aa";  // expected false
    	//String s = "aa", p = "*";    // expected true
    	//String s = "aa", p = "a*";   // expected true

    	//String s = "ab", p = "?*";  // expected true

    	//String s = "aab", p = "c*a*b";  // expected false

    	//String s = "aab", p = "*a*";  // expected true
    	
    	//String s = "aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba", p = "a*******b";  // expected false
    	
    	String s = "bbbaaabaababbabbbaabababbbabababaabbaababbbabbbabb", p = "*b**b***baba***aaa*b***"; 

    	
    	WildcardMatching solution = new WildcardMatching();
    	System.out.println(solution.isMatch(s, p));
	}

}





