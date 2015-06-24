/**
 * https://leetcode.com/problems/dungeon-game/
 * 
 * 
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Mar 8, 2015
 */
public class DungeonGame {

	
    public int calculateMinimumHP(int[][] dungeon) {
    	int rows = dungeon.length;
    	int cols = dungeon[0].length;
    	
    	int [][] minHP = new int[rows][cols];
    	int [][] remainHP = new int[rows][cols];
    	
    	// Initialize the remaining HP and minimal initial HP for each cell.
    	remainHP[0][0] = dungeon[0][0];
    	minHP[0][0] = dungeon[0][0] < 0 ? dungeon[0][0] : 0;
    	
    	for (int i=1; i<cols; ++i) {
    		remainHP[0][i] = remainHP[0][i-1] + dungeon[0][i];
    		minHP[0][i] = Math.min(minHP[0][i-1], remainHP[0][i]);
    	}
    	
    	for (int j=1; j<rows; ++j) {
    		remainHP[j][0] = remainHP[j-1][0] + dungeon[j][0];
    		minHP[j][0] = Math.min(minHP[j-1][0], remainHP[j][0]);
    	}
    	
    	for (int r=1; r<rows; ++r) {
    		
    		for (int c=1; c<cols; ++c) {
    			
    			// Two remaining candidates
    			int up   = dungeon[r][c] + remainHP[r-1][c];
    			int left = dungeon[r][c] + remainHP[r][c-1];
    			
    			// Two minHP candidate
    			int upMin = Math.min(minHP[r-1][c], up);
    			int leftMin = Math.min(minHP[r][c-1], left);
    			
    			// Find a candidate that requires less initial HP
    			if (upMin < leftMin) {
    				minHP[r][c] = leftMin;
    				remainHP[r][c] = left;
    				
    			} else {
    				minHP[r][c] = upMin;
    				remainHP[r][c] = up;
    			}
    		}
    	}
    	
    	return minHP[rows-1][cols-1] > 0 ? 1 : 1-minHP[rows-1][cols-1];
    }
	
    
    
	
	/*
	int _minHP = Integer.MIN_VALUE;
	
	private void move(int [][] dungeon, 
			int r, int c, int remainHP, int minHP) {
		

		remainHP = dungeon[r][c] + remainHP;
		minHP = remainHP < 0 ? Math.min(remainHP, minHP) : minHP;

		if ( r == dungeon.length - 1 &&
			 c == dungeon[0].length - 1) {
			
			_minHP = Math.max(minHP, _minHP);
			return;
		}

		if (r < dungeon.length-1) {
			move(dungeon, r+1, c, remainHP, minHP);
		}
		
		if (c < dungeon[0].length-1) {
			move(dungeon, r, c+1, remainHP, minHP);
		}
		
	}
	
	public int calculateMinimumHP(int[][] dungeon) {
		move(dungeon, 0, 0, 0, 0);
		return -_minHP + 1;
	}
	
	*/
	
	
	public static void main(String[] args) {
		
		/*
		int [][] dungeon = 
			{{-2, -3, 3},
			 {-5, -10, 1},
		     {10, 30, -5}};
		// expected 7 
		*/
		
		int [][] dungeon = {{1,-3,3},{0,-2,0},{-3,-3,-3}};
		// expected 3
		
		//int [][] dungeon = {{100}};  // expected 1
		
		DungeonGame dg = new DungeonGame();
		
		System.out.println(dg.calculateMinimumHP(dungeon));
	}

}







