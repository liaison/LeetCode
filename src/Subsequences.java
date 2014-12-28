
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
	

	/** dp[i][j] represents the number of solutions of aligning substring T[0..i] with S[0..j]; 
	 *
	 *  dp[0][j] = 1, since aligning T = "" with any substring of S 
	 *  				would have only ONE solution which is to delete all characters in S.  
	 *
	 *  dp[i][j]:  if T[i] != S[j], then the solution would be to ignore the character S[j] and 
	 *  				align substring T[0..i] with S[0..(j-1)].
	 *    				therefore, dp[i][j] = dp[i][j-1].
	 *    
	 *    		   if T[i] == S[j], then first we could adopt the above solution, but also 
	 *    				we could match the characters T[i] and S[j] and 
	 *    				align the rest of them (i.e. T[0..(i-1)] and S[0..(j-1)]. 
	 *    				therefore, dp[i][j] = dp[i][j-1] + d[i-1][j-1]
	 *    
	 *  e.g.     T = B, S = ABC
	 *  
	 *  dp[1][2]=1:  Align T'=B and S'=AB, only one solution, remove character A in S'.     
	 *  
	 */
	public int numDistinct(String S, String T) {
		int sl = S.length();
		int tl = T.length();
		
		int [][] dp = new int[tl+1][sl+1];
    
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
    
	public int numDistinct_sdp(String S, String T) {
		int sl = S.length();
		int tl = T.length();
		
		int [] preComb = new int[sl+1];
		int [] comb = new int[sl+1];
		
		
		for(int i=0; i<=sl; i++)
			preComb[i] = 1;		
	
		for(int t=1; t<=tl; ++t){
			for(int s=1; s<=sl; ++s){
				if(T.charAt(t-1) != S.charAt(s-1)){
					comb[s] = comb[s-1];
				}else{
					comb[s] = comb[s-1] + preComb[s-1];
				}
			}
			
			for(int i=0; i<=sl; ++i){
				preComb[i] = comb[i];
			}
		}
		
		return preComb[sl];
	}
    
	
    public static void main(String[] args) {
    	String S = "rabbbit";
    	String T = "rabbit";

    	Subsequences solution = new Subsequences();
    	System.out.println(solution.numDistinct_sdp(S, T));    			
	}

}







