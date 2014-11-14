import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;


/**
 * 

You are given a string, S, and a list of words, L, that are all of the same length. 
Find all starting indices of substring(s) in S that is a concatenation of each word 
in L exactly once and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).

Note: the words in the list L do NOT have to be UNIQUE.

 * 
 * 
 * @author Lisong Guo <lisong.guo@inria.fr>
 * @date   Nov 13, 2014
 *
 */

public class SubstringOps {
    
	public List<Integer> findSubstring(String S, String[] L) {
		List<Integer> res = new LinkedList<Integer>();
		
		int WORD_SIZE = 0;
		
		if(L.length == 0 || S.length() == 0){
			return res;
		}else{
			WORD_SIZE = L[0].length();
		}
		
		ArrayList<Integer> slide_window = new ArrayList<Integer>();
		HashMap<String, Integer> last_match = new HashMap<String, Integer>();
		
		Arrays.sort(L);
		
		int index = 0;
		while(index < S.length()){

			boolean isMatch = true;
			slide_window.clear();
			last_match.clear();
			
			for(int i=0; i<L.length; i++){
				
				Integer lmp = last_match.get(L[i]);
				
				int entry = 0;
				
				if(lmp != null){
					// proceed to next word (WORD_SIZE), instead of letter (1)
					entry = S.indexOf(L[i], lmp+WORD_SIZE);
				}else{
					entry = S.indexOf(L[i], index);
				}
				
				slide_window.add(entry);
				last_match.put(L[i], entry);
			}
			
			Collections.sort(slide_window);
			Integer prev = Integer.MIN_VALUE;
			
			for(Integer iter : slide_window){

				if(iter == -1){
					// one of the words is missing from the slide window
					return res;
				}
				
				if(prev == Integer.MIN_VALUE){
					prev = iter;
					continue;
				}
				
				if(iter != prev + WORD_SIZE){
					isMatch = false;
					break;
				}
				
				prev = iter;
			}
			
			if(isMatch){
				res.add(slide_window.get(0));
			}
			
			// Proceed by letter, since words can overlap! 
			index = index + 1;
		
			// Proceed word by word, if found match, since matches can overlap!
			//index = slide_window.get(0) + WORD_SIZE;
		
			// Alternative (efficient but not right), proceed by slide window. 
			//index = slide_window.get(slide_window.size()-1) + 1;
		
		}
		
		return res;
    }
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		//String S = "barfoothefoobarman";
		//String [] L = {"foo", "bar"};
		
		// Time Limit Exceeded 
		//String S = "lingmindraboofooowingdingbarrwingmonkeypoundcake";
		//String [] L = {"fooo","barr","wing","ding","wing"};
		
		// The matched word list can overlap with each other.
		//String S = "aaa";
		//String [] L = {"a", "a"};
		
		//String S = "aaaaaa";
		//String [] L = {"aaa", "aaa"};
		
		String S = "abaababbaba";
		String [] L = {"ab","ba","ab","ba"};
		
		
		SubstringOps solution = new SubstringOps();
		Utils.printList(solution.findSubstring(S, L));
		
	}

}



