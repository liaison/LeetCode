
/**
 * 
 * Given a string, determine if it is a palindrome, 
 	considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

 * 
 * @author Lisong Guo <lisong.guo@inria.fr>
 * @date   Nov 07, 2014
 *
 */
public class Palindrome {

	 public boolean isPalindrome(String s) {
	     if(s.isEmpty()){
	    	 return true;
	     }
	     
	     s = s.toLowerCase();
	     int h = 0, t = s.length()-1;
	     
	     while(h < t){
	    	 if(! Character.isLetterOrDigit(s.charAt(h))){
	    		 ++h; 
	    		 continue;
	    	 }
	    	 
	    	 if(('a' > s.charAt(t) || s.charAt(t) > 'z') && 
	    	    ('0' > s.charAt(t) || s.charAt(t) > '9')){
	    		 --t;
	    		 continue;
	    	 }
	    	 
	    	 if(s.charAt(h) != s.charAt(t)){
	    		 return false;
	    	 }else{
	    		 ++h;
	    		 --t;
	    	 }
	     }
	     
		 return true;
	 }
	
	 public boolean isPalindrome_2(String s) {
	        s = s.toLowerCase(); // convert all to lower cases.
	        s = s.replaceAll("[^a-z^0-9]+", ""); // remove all non-digital and non-letter.
	        int len = s.length();
	        for (int i = 0; i < len; i++){
	            if (s.charAt(i) != s.charAt(len - i - 1)){
	                return false;
	            }
	        }
	        return true;
	 }
	 
	 
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		//String a = "race a car";
		//String a = "A man, a plan, a canal: Panama";
		//String a = "1a2";
		//String a = ".a"; // true
		String a = "ab";
		
		Palindrome solution = new Palindrome();
		
		System.out.println(solution.isPalindrome(a));
	}

}
