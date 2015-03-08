/**
 * https://leetcode.com/problems/dungeon-game/
 * 
 * 
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Mar 8, 2015
 */
public class DungeonGame {

	
	/*
    public int calculateMinimumHP(int[][] dungeon) {
    	int rows = dungeon.length;
    	int cols = dungeon[0].length;
    	
    	int [][] minHP = new int[rows][cols];
    	int [][] remainHP = new int[rows][cols];
    	
    	
    	for (int r=0; r<rows; ++r) {
    		for (int c=0; c<cols; ++c) {
    			
    			int min = dungeon[r][c];
    			
    			if (r-1 >= 0) {
    			    min = dungeon[r][c] + dungeon[r-1][c];
    			}
    			
    			if (c-1 >= 0) {
    				min = Math.max(min, dungeon[r][c] + dungeon[r][c-1]);
    			}
    			
    			minHP[r][c] = min;
    		}
    	}
    	
    	return -dungeon[rows-1][cols-1] + 1;
    }
	*/
	
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
	
	public static void main(String[] args) {
		int [][] dungeon = 
			{{-2, -3, 3},
			 {-5, -10, 1},
		     {10, 30, -5}};
	
		DungeonGame dg = new DungeonGame();
		
		System.out.println(dg.calculateMinimumHP(dungeon));
	}

}







