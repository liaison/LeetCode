
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
	 * Determine whether an integer is a palindrome. 
	 * 	
	 * Note: negative number is not considered to be palindrome.
	 * 
	 * Do this without extra space.
	 */
	public boolean isPalindrome(int x) {
		long rdiv = 1;
		long ldiv = 10; // overflow! the highest position in x.
		if(x < 0)
			return false;
		else if(x < 10)
			return true;
		
		while( (x/ldiv) > 9 ){
			ldiv *= 10;
		}
		
		while(ldiv > 9){
			// extract digits based on the divisions, 
			//		without changing the value of x.
			int l = (int)(x/ldiv)%10;
			int r = (int)(x/rdiv)%10;
			
			if(l != r)
				return false;
			// shift two digits
			ldiv /= 10;
			rdiv *= 10;
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
	
		//int x = 10; //expected false
		//int x = 1; // expected true;
		//int x = 11211; 
		//int x = -2147483648; // overflow? expected false
		//int x = 1000021;     // tricky case, expected false
		int x = 1002001;     // tricky case, expected true
		
		//int x = -212; 
		
		System.out.println(String.valueOf(x) + ":" + 
							solution.isPalindrome(x));
	}

}
