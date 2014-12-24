import java.util.Stack;


/**
 * 
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".


Clarification:

What constitutes a word?
	A sequence of non-space characters constitutes a word.

Could the input string contain leading or trailing spaces?
	Yes. However, your reversed string should not contain leading or trailing spaces.

How about multiple spaces between two words?
	Reduce them to a single space in the reversed string.

 * @author Lisong Guo <lisong.guo@me.com>
 * @date   24 Dec, 2014
 *
 */


public class ReverseWords {
    
	
	public String reverseWords(String s) {
		int size = s.length();
		if(size == 0)
			return "";
		
		Stack<String> words = new Stack<String>();
		StringBuffer word = new StringBuffer();
		for(int i=0; i<size; i++){
			char c = s.charAt(i);
			if(c == ' '){
				if(word.length() > 0){
					words.push(word.toString());
					word.delete(0, word.length());
				}
			}else{
				word.append(c);
			}
		}
		
		if(word.length() > 0)
			words.push(word.toString());
		
		size = words.size();
		StringBuffer res = new StringBuffer();
		for(int i=0; i<size-1; i++){
			res.append(words.pop());
			res.append(" ");
		}
		
		if(words.size() == 1){
			res.append(words.pop());	
		}
		
		return res.toString();
    }
    
    
	public static void main(String[] args) {
		String s = "the sky is blue";
		//String s = " ";
		
		ReverseWords solution = new ReverseWords();
		System.out.println(solution.reverseWords(s));
	}

}










