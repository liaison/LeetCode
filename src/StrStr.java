import java.util.Hashtable;



/**
 * 
 * Implement strStr().
 * 
 *  Returns the index of the first occurrence of needle in haystack, 
 *  or -1 if needle is not part of haystack.
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Dec 28, 2014
 *
 */
public class StrStr {

    /**
     *  Native implementation

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

    
    /**
     * Calculate the minimal distance of a character to the end of the string.
     * This captures the features / pattern of a string to be matched.
     * For instance,  a string like "ABC" would be matched faster than the one
     *  such as "AAA", since we could not shift big steps for "AAA", but moving
     *  one step after another.
     */
    private void preBadChar(String p){
    	bcTable = new Hashtable<Character, Integer>();
    	
    	int s = p.length();
        // The minimal distance between a character and the end of the string.
        // e.g.  REPEAT:
        //   bcTable(R) = 5, since there is no R following.
        //   bcTable(E) = 2, the most recent appearance of E is at the position 3
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

            // do the match in the reverse order,
            // i.e. from the bottom of the string
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
 
            // When exiting from the above reverse match,
            //  we get the mismatched character "b" in the haystack,
            //  then for the next possible match, we could at least
            //  reserve the distance of bcTable("b"), i.e. we could
            //  shift bcTable("b") steps for the next match.
            Integer shift = bcTable.get(haystack.charAt(i+nl-1));
            if(shift == null){
                // really bad character
                i += nl;
            }else{
                i += shift;
            }
        }

        // Did not find any match
    	return -1;
    }
    
    public static void main(String[] args) {
        String haystack = "thisisaneedleinahaystack";
        String needle = "needle";
        StrStr solution = new StrStr();
        System.out.println(solution.strStr(haystack, needle));
    }
}

