
/**

Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string 
by deleting some (can be none) of the characters without 
disturbing the relative positions of the remaining characters. 
(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
	S = "rabbbit", T = "rabbit"

	Return 3.

In other words, how many combination are there in sequence S that can form the sequence T. 

    S1= "ra_bbit" S2= "rab_bit" S3="rabb_it"

 * 
 * 
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Dec 28, 2014
 */

public class Subsequences {
	
	
	public int numDistinct(String S, String T) {
		int sl = S.length();
		int tl = T.length();
		
		int [][] dp = new int[tl+1][sl+1];
    
		/** dp[i][j] represents the solution of aligning substring T[0..i] and S[0..j]; 
		 *
		 *  dp[0][j] = 1, since aligning T = "" with any substring of S 
		 *  				would have only ONE solution -- delete all characters in S  
		 *
		 *  dp[i][j]:  if T[i] != S[j], then the solution would be to ignore the character S[j] and 
		 *  				align substring T[0..i] with S[0..(j-1)].
		 *    
		 *    		   if T[i] == S[j], then first we could adopt the above solution, but also 
		 *    				we could match the characters T[i] and S[j] and 
		 *    				align the rest of them (i.e. T[0..(i-1)] and S[0..(j-1)]. 
		 *    
		 *  e.g.    S = ABC,  T = B
		 *  
		 *  dp[1][2]:  S'=AB, T'=B   
		 *  
		 */
		for(int i=0; i<=sl; ++i){
			dp[0][i] = 1;
		}
		
		for(int t=1; t<=tl; ++t){
			
			for(int s=1; s<=sl; ++s){
				if(T.charAt(t-1) != S.charAt(s-1)){
					dp[t][s] = dp[t][s-1];
				}else{
					dp[t][s] = dp[t][s-1] + dp[t-1][s-1];
				}
			}	
		}
		
		return dp[tl][sl];
	}
    
	
    public static void main(String[] args) {
    	String S = "rabbbit";
    	String T = "rabbit";

    	Subsequences solution = new Subsequences();
    	System.out.println(solution.numDistinct(S, T));
    			
	}

}







