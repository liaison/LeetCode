
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

	/**
	 * The result is basically Yang Hui's triangle, 
	 * 		which is also applied in binomial combination. 
	
	public int uniquePaths(int m, int n) {
		
	}
	 */
	
    
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
    
    
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
    	if(obstacleGrid == null){
    		return 0;
    	}
    	
    	int m = obstacleGrid.length;
    	int n = obstacleGrid[0].length;
    	
    	int [][] dp = new int[m][n];
    	
    	for(int i=0; i<m; i++){
    		for(int j=0; j<n; j++){
    			if(obstacleGrid[i][j] == 1){
    				// the path is blocked, so no path
    				dp[i][j] = 0;
    				continue;
    			}
    			
    			if(i == 0 && j == 0){
    				dp[0][0] = 1;
    			
    			}else if(i == 0){ // j != 0 
    				dp[i][j] = dp[i][j-1];
    			
    			}else if(j == 0){ // i != 0
    				dp[i][j] = dp[i-1][j];
    				
    			}else{ // i != 0 && j != 0
    				dp[i][j] = dp[i-1][j] + dp[i][j-1];
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
		
		int [][] obstacleGrid = {{0,0,0},
		                         {0,1,0},
		                         {0,0,0}};
		
		System.out.println(solution.uniquePathsWithObstacles(obstacleGrid));	
	}

}







