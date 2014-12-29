import java.util.Hashtable;



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

	/**
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
    */
    
    private Hashtable<Character, Integer> bcTable;
    
    private void preBadChar(String p){
    	bcTable = new Hashtable<Character, Integer>();
    	
    	int s = p.length();
    	for(int i=0; i<s-1; ++i){
    		bcTable.put(p.charAt(i), s-i-1);
    	}
    }
	
    public int strStr(String haystack, String needle) {
    	this.preBadChar(needle);
    	
    	int hl = haystack.length();
    	int nl = needle.length();
    	int i = 0;
    	while(i <= hl-nl){
    		int j = nl-1;
    		while(j >= 0){
    			if(haystack.charAt(i+j) != needle.charAt(j)){
    				break;
    			}
    			--j;
    		}
    		
    		if(j < 0){
    			// find match
    			return i;
    		}
    		
    		// Not a match, shift to another position
    		Integer shift = bcTable.get(haystack.charAt(i+nl-1));
    		if(shift == null){
    			// really bad character
    			i += nl;
    		}else{
    			i += shift;
    		}
    	}
    	
    	return -1;
    }
    
    
	public static void main(String[] args) {
		String haystack = "thisisaneedleinahaystack";
		String needle = "needle";
		StrStr solution = new StrStr();
		
		System.out.println(solution.strStr(haystack, needle));
	}

}
