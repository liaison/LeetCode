import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
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
    
	/**
	public List<Integer> findSubstring(String S, String[] L) {
		
		int WORD_SIZE = 0;
		int WORD_NUM = 0;
		int INPUT_SIZE = S.length();
		
		if(L.length == 0 || INPUT_SIZE == 0){
			return new LinkedList();
		}else{
			WORD_SIZE = L[0].length();
			WORD_NUM = L.length;
		}
		
		HashSet<Integer> res = new HashSet<Integer>();
		
		ArrayList<Integer> slide_window = new ArrayList<Integer>();
		HashMap<String, Integer> last_match = new HashMap<String, Integer>();
		
		Arrays.sort(L);
		
		int index = 0;
		while(index <= INPUT_SIZE - WORD_SIZE * WORD_NUM){

			boolean isMatch = true;
			slide_window.clear();
			last_match.clear();
			
			for(int i=0; i<L.length; i++){
				
				Integer lmp = last_match.get(L[i]);
				
				int entry = 0;

				if (lmp != null) {
					// proceed to next word (WORD_SIZE), instead of letter (1)
					entry = S.indexOf(L[i], lmp + WORD_SIZE);
				} else {
					entry = S.indexOf(L[i], index);
				}

				
				// check overlapping with existing matching of words				
				for (Integer range : slide_window) {
					if (range <= entry && entry <= range + WORD_SIZE) {
						// re-generate entry
						entry = S.indexOf(L[i], range + WORD_SIZE);
					}else if(entry == -1){
						break;
					}
				}

				if(entry == -1){
					// one of the words is missing from the slide window, 
					//   early exit, good for performance. 
					LinkedList<Integer> l = new LinkedList<Integer>();
					l.addAll(res);
					return l;
				}
				
				slide_window.add(entry);
				last_match.put(L[i], entry);
			}
			
			Collections.sort(slide_window);
			Integer prev = Integer.MIN_VALUE;
			
			for(Integer iter : slide_window){

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
			index = slide_window.get(0) + 1;
		
			// Proceed word by word, if found match, since matches can overlap!
			//index = slide_window.get(0) + WORD_SIZE;
		
			// Alternative (efficient but not right), proceed by slide window. 
			//index = slide_window.get(slide_window.size()-1) + 1;
		
		}
		
		LinkedList<Integer> l = new LinkedList<Integer>();
		l.addAll(res);
		return l;
    }
	*/
	
	/**
	 *  Do NOT use string.indexOf()
	 */
    
	public List<Integer> findSubstring(String S, String[] L) {
	
		int WORD_SIZE = 0;
		int WORD_NUM = 0;
		int INPUT_SIZE = S.length();
		LinkedList<Integer> res = new LinkedList<Integer>();
		
		if(L.length == 0 || INPUT_SIZE == 0){
			return res;
		}else{
			WORD_SIZE = L[0].length();
			WORD_NUM = L.length;
		}
		
		HashMap<String, Integer> words = new HashMap<String, Integer>();
		HashMap<String, Integer> slide_window = new HashMap<String, Integer>();
		
		// Build dictionary
		for(int i=0; i<L.length; i++){
			Integer count = words.get(L[i]);
			if(count == null){
				words.put(L[i], 1);
			}else{
				words.put(L[i], count+1);
			}
		}
		
		int index = 0;
		while(index <= INPUT_SIZE - WORD_SIZE*WORD_NUM){
			slide_window.clear();
			
			boolean isMatch = true;
			
			for(int p = 0; p < WORD_NUM; p++){
				String token = S.substring(index+p*WORD_SIZE, index+(p+1)*WORD_SIZE);
				
				Integer wc = words.get(token);
				if(wc == null){
					// This slide window will NOT work
					isMatch = false;
					break;
				}else{
					Integer c = slide_window.get(token);
					if(c == null){
						slide_window.put(token, 1);
					}else{
						slide_window.put(token, c+1);
					}
					
					// Not need to check the match between slide_window and words afterwards
					if(slide_window.get(token) > wc){
						isMatch = false;
						break;
					}
				}
			}
			

			if(isMatch){
				res.add(index);
			}
			
			index ++;
		}
		
		return res;
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		//String S = "barfoothefoobarman";
		//String [] L = {"foo", "bar"};		// expected {0, 9}
		
		// Time Limit Exceeded 
		String S = "lingmindraboofooowingdingbarrwingmonkeypoundcake";
		String [] L = {"fooo","barr","wing","ding","wing"};   // expected {13}
		
		// The matched word list can overlap with each other.
		//String S = "aaa";
		//String [] L = {"a", "a"};			// expected {0, 1}
		
		//String S = "aaaaaa";
		//String [] L = {"aaa", "aaa"};		// expected {0}
		
		//String S = "abaababbaba";
		//String [] L = {"ab","ba","ab","ba"};  // expected {1, 3}
		
		
		SubstringOps solution = new SubstringOps();
		Utils.printList(solution.findSubstring(S, L));
		
	}

}



