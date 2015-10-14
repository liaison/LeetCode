import org.junit.Test;



/**
 * https://leetcode.com/problems/game-of-life/

According to the Wikipedia's article:
 "The Game of Life, also known simply as Life, is a cellular automaton 
   devised by the British mathematician John Horton Conway in 1970."

	Given a board with m by n cells, each cell has an initial state live (1) 
	or dead (0). Each cell interacts with its eight neighbors (horizontal, 
	vertical, diagonal) using the following four rules
	 (taken from the above Wikipedia article):

- Any live cell with fewer than two live neighbors dies,
	as if caused by under-population.
	
- Any live cell with two or three live neighbors lives on to the next generation.

- Any live cell with more than three live neighbors dies,
	as if by over-population..

- Any dead cell with exactly three live neighbors becomes a live cell,
	as if by reproduction.

Write a function to compute the next state (after one update)
	of the board given its current state.

Follow up: 
	* Could you solve it in-place? Remember that the board needs to be
   		updated at the same time: You cannot update some cells first and
   		then use their updated values to update other cells.

	* In this question, we represent the board using a 2D array.
	   In principle, the board is infinite, which would cause problems when
	   the active area encroaches the border of the array. How would you 
	   address these problems?
 
 */
public class GameOfLife {

	@Test
	public void testGameOfLife() {
		int [][] board = {{0, 0, 0, 0, 0},
		     			  {0, 1, 1, 0, 0},
						  {1, 0, 0, 1, 0},
						  {0, 1, 1, 1, 1}};
		
		GameOfLife gol = new GameOfLife();
		
		gol.gameOfLife(board);
		
		Utils.printMatrix(board);
	}
	
	
    public void gameOfLife(int[][] board) {
        int rows = board.length;
        int cols = board[0].length;
        
        int [][] board_next = board.clone();

		int upleft=0, up=0, upright=0, left=0,
		    right=0, downleft=0, down=0, downright=0;

		int lives = 0;

    	for (int r = 0; r < rows; ++ r) {
    		
    		for (int c = 0; c < cols; ++ c) {
    			
    			if (r-1 < 0) {
    				up = 0;
    				upleft = 0;
    				upright = 0;
    			} else if (r+1 >= rows) {
    				down = 0;
    				downleft = 0;
    				downright = 0;
    			} else {
    				up   = board[r-1][c];
    				down = board[r+1][c];
    			}
    			
    			if (c-1 < 0) {
    				upleft = 0;
    				left = 0;
    				downleft = 0;
    			} else if (c+1 >= cols) {
    				upright = 0;
    				right = 0;
    				downright = 0;
    			} else {
    				left  = board[r][c-1];
    				right = board[r][c+1];
    			}
    			
    			if (r - 1 >= 0 && c - 1 >= 0) {
    				upleft = board[r-1][c-1];
    			} else {
    				upleft = 0;
    			}
    			
    			if (r - 1 >= 0 && c + 1 < cols) {
    				upright = board[r-1][c+1];
    			} else {
    				upright = 0;
    			}
    			
    			if (r+1 < rows && c-1 >= 0) {
    				downleft = board[r+1][c-1];
    			} else {
    				downleft = 0;
    			}
    			
    			if (r + 1 < rows && c + 1 < cols) {
    				downright = board[r+1][c+1];
    			} else {
    				downright = 0;
    			}
    			
    			
    			lives = upleft + up + upright +
    				    left 	 +    right +
    				    downleft + down + downright;
    			
    			switch(lives) {
    				case 0:
    				case 1:
    					// Fewer than two neighbors lives --> dead (underpopulation)
    					board_next[r][c] = 0;
    					break;
    				case 2:
    					// unchanged, dead remains dead, life lives on.
    					break;
    				case 3:
    					// Reproduction
    					board_next[r][c] = 1;
    					break;
    				case 4:
    				case 5:
    				case 6:
    				case 7:
    				case 8:
    					// More than 3 lives --> dead (overpopulation)
    					board_next[r][c] = 0;
    					break;
    			}
    		}
    	}
    	
    	// Update the results to the original board.
    	for(int r=0; r<rows; ++r) {
    		for(int c=0; c<cols; ++c) {
    			board[r][c] = board_next[r][c];
    		}
    	}
    }


}
