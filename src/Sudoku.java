/**
 * 

Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
 
 * @author Lisong Guo <lisong.guo@inria.fr>
 * @date   Nov 15, 2014
 *
 */
public class Sudoku {


    public void solveSudoku(char[][] board) {
        
    }
    
    
    /**
     * Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
     * 	http://sudoku.com.au/TheRules.aspx
     * 
	 *  The Sudoku board could be partially filled, 
	 * 		where empty cells are filled with the character '.'.
	 * Note:
	 * 		A valid Sudoku board (partially filled) is not necessarily solvable. 
	 * 		Only the filled cells need to be validated.
	 * 
	 * Another reference solution, exchange space with simplicity. 
	 * 		https://oj.leetcode.com/discuss/23901/my-short-solution-by-c-o-n2
     */
    public boolean isValidSudoku(char[][] board) {
        
        // Check the rows 
        for(char [] row : board) {
        	// reset the bit map before checking
        	if(! checkBlock(row)) {
        		return false;
        	}
        }
        
        // Check the columns 
        char [] block = new char[9];
        for(int i=0; i<9; ++i) {
        	for(int j=0; j<9; ++j) {
        		block[j] = board[j][i];
        	}
        	
        	if(! checkBlock(block)) {
        		return false;
        	}
        }
        
        // Check the sub-blocks within the grid
        for(int i=0; i<9; ++i) {
        	for(int j=0; j<3; ++j) {
        		for(int k=0; k<3; ++k) {
        			block[j*3+k] = board[(i/3)*3+j][k+(i%3)*3];
        		}
        	}
        	
        	if(! checkBlock(block)) {
        		return false;
        	}
        }
        
        return true;
    }

    private boolean checkBlock(char [] block) {
    	int[] bmap  = new int[10];
    	for(char c : block) {
    		if(c == '.') continue;
    		if(bmap[c-'0'] == 1) {
    			return false;  // Find a duplicate.
    		} else {
    			bmap[c-'0'] = 1;
    		}
    	}
    	return true;
    }
    
    
    
	public static void main(String[] args) {
		 String [] input = {".21......",
				 			"....6....",
				 			"......7..",
				 			"....5....",
				 			"..5......",
				 			"......3..",
				 			".........",
				 			"3...8.1..",
				 			"........8"};  // expect true;
		 char [][] board = Utils.string2matrix(input);
		 Sudoku solution = new Sudoku();
		 
		 System.out.println(solution.isValidSudoku(board));
	}

}












