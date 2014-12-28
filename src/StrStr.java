

/**
 * 
 * Implement strStr().
 * 
   Returns the index of the first occurrence of needle in haystack, 
    or -1 if needle is not part of haystack.

 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Dec 28, 2014
 *
 */
public class StrStr {

    public int strStr(String haystack, String needle) {
    	int nl = needle.length();
    	int hl = haystack.length();
    	
    	for(int i=0; i<=hl-nl; i++){
    		
    		if(haystack.substring(i, i+nl).equals(needle)){
    			return i;
    		}
    	}
    	
    	return -1;
    }
	
	public static void main(String[] args) {
		String haystack = "thisisaneedle";
		String needle = "needle";
		StrStr solution = new StrStr();
		
		System.out.println(solution.strStr(haystack, needle));
	}

}
