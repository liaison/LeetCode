
/**
 * A robot is located at the top-left corner of a m x n grid 
 * 	(marked 'Start' in the diagram below).

	The robot can only move either down or right at any point in time. 
	The robot is trying to reach the bottom-right corner of the grid 
	(marked 'Finish' in the diagram below).

	How many possible unique paths are there?
 
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Dec 14, 2014
 *
 */
public class UniquePath {

    public int uniquePaths(int m, int n) {
    	if(m == 0 || n == 0){
    		return 0;
    	}
    	
    	int [][] dp = new int[m][n];
    	
    	for(int i=0; i<m; i++){
    		dp[i][0] = 1;
    		
    		for(int j=1; j<n; j++){
    			if(i == 0){
        			dp[0][j] = 1;
        		}else{	
        			dp[i][j] = dp[i][j-1] + dp[i-1][j]; 
        		}
    		}
    	}
    	
    	return dp[m-1][n-1];
    }
    
    
	/**
	 * @param args
	 */
	public static void main(String[] args) {

		UniquePath solution = new UniquePath();
		System.out.println(solution.uniquePaths(3,  2));
	}

}
