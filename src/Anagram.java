import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Iterator;
import java.util.List;

/**
 * Two words are anagram, if they contain the same set and number of characters.
 * 
 * e.g.  Tim, MIT, TMI 
 *  
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Jan 04, 2014
 *
 */
public class Anagram {

	/**
	 * Given an array of strings, return all groups of strings that are anagrams.
	   Note: All inputs will be in lower-case.
	 */
    public List<String> anagrams(String[] strs) {
        HashMap<String, ArrayList<Integer>> hashmap = 
        		new HashMap<String, ArrayList<Integer>>();
        ArrayList<String> res = new ArrayList<String>();
        // build a hash table, with the "unique" string form as the key
        for(int i=0; i<strs.length; ++i){
        	char [] charArray = strs[i].toCharArray();
        	Arrays.sort(charArray);
        	String key = String.valueOf(charArray);
        	
    		ArrayList<Integer> value = hashmap.get(key);
        	if(value == null){
        		value = new ArrayList<Integer>();
        		value.add(i);
        		hashmap.put(key, value);
        	}else{
        		value.add(i);
        	}
        }
        
        // extract anagrams from the hash table.
        Iterator<String> iter = hashmap.keySet().iterator();
        while(iter.hasNext()){
        	ArrayList<Integer> indexList = 
        			hashmap.get(iter.next());
        	if(indexList.size() > 1){
        		for(Integer i : indexList){
            		res.add(strs[i]);
            	}
        	}
        }
        
        return res;
    }
    
    
	public static void main(String[] args) {
		String [] strs = {"tim", "mit", "abc", "c"};
		
		Anagram solution = new Anagram();
		List<String> res = solution.anagrams(strs);
		for(int i=0; i<res.size(); ++i){
			System.out.println(res.get(i));
		}
	}

}
