
/**
 * 
 * Convert a string that represents a decimal number to an integer. 
 * 
 * Note: overflow isse
 * 
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Dec 30, 2014
 *
 */

public class Atoi {
	private static int maxDiv10 = Integer.MAX_VALUE/10; 
	
	public int atoi(String s){
		int num = 0;
		int i = 0;
		boolean isPos = true;
		
		while(s.charAt(i) == ' ') ++i;
		
		if(s.charAt(i) == '-') isPos = false;
		
		while(i < s.length()){
			int digit = s.charAt(i) - '0';
			
			if(0 <= digit && digit <= 9){
				// overflow check
				if(num > maxDiv10 || (num == maxDiv10 && digit >= 8)){
					return isPos ? Integer.MAX_VALUE : Integer.MIN_VALUE;
				}
				
				num = num * 10 + digit;
			}
			
			++i;
		}
		
		return isPos ? num : -num;
	}
	
	
	public static void main(String[] args) {
		String s = "-13333323";
		Atoi solution = new Atoi();
		
		System.out.println(solution.atoi(s));
	}

}
