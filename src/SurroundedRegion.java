import java.util.HashSet;
import java.util.Iterator;
import java.util.LinkedList;


/**
 * 

Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

 * 
 * @author Lisong Guo<lisong.guo@inria.fr>
 * @date   Nov 23, 2014
 *
 */


public class SurroundedRegion {

	
    public void solve(char[][] board) {
    	if(board == null || board.length == 0){
    		return;
    	}
    	
    	HashSet<Integer> Oset = new HashSet<Integer>();
    	int rowSize = board.length;
    	int columnSize = board[0].length;
    	
    	// Identify 'O' and put them into a set
    	for(int i=0; i<board.length; i++){
    		for(int j=0; j<board[i].length; j++){
    			if(board[i][j] == 'O'){
    				Oset.add(i*columnSize + j);
    			}
    		}
    	}
    	
    	// Explore the space
    	while(true){
        	Iterator<Integer> iter = Oset.iterator();
        	if(!iter.hasNext()){
        		break;
        	}
        	
    		int k = iter.next();
    		LinkedList<Integer> explorer = new LinkedList<Integer>();
    		explorer.add(k);
    		LinkedList<Integer> space = new LinkedList<Integer>(); 
    		
    		boolean isCaptured = true;
    		while(! explorer.isEmpty()){
    			int p = explorer.poll();
    			Oset.remove(p);
    			space.add(p);
    			
				// reach the boundary, therefore no capture. 
    			if(p % columnSize == 0  ||
    			   p % columnSize == columnSize-1 ||
    			   p / columnSize == 0 ||
    			   p / columnSize == rowSize-1 ){
    				isCaptured = false;
    			}
    			
    			
    			// check the next element on the left
				if(Oset.contains(p-1)){
					explorer.add(p-1);
					Oset.remove(p-1);
				}
				
    			// check the next element on the right
				if(Oset.contains(p+1)){
					explorer.add(p+1);
					Oset.remove(p+1);
				}

				// check the element on the previous row
				if(Oset.contains(p-columnSize)){
					explorer.add(p-columnSize);
					Oset.remove(p-columnSize);
				}
				
				
				// check the element on the next row
				if(Oset.contains(p+columnSize)){
					explorer.add(p+columnSize);
					Oset.remove(p+columnSize);
				}
				
    		}
    		
    		if(isCaptured){
    			// set the space 'O' to 'X'.
    			for(Integer p : space){
    				board[p/columnSize][p%columnSize] = 'X';
    			}
    		}
    	}
    }
	
    
    public void printBoard(char [][] board){
    	for(int i=0; i<board.length; i++){
    		for(int j=0; j<board[i].length; j++){
    			System.out.print(board[i][j] + " ");
    		}
    		System.out.println();
    	}
    }
    
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		/*
		char [] [] board = {{'X', 'X', 'X', 'X'}, 
							{'X', 'O', 'O', 'X'},
							{'X', 'X', 'O', 'X'},
							{'X', 'O', 'X', 'X'}};
		
		char [] [] board = {{'X', 'X', 'X', 'X'}, 
							{'X', 'O', 'O', 'O'},
							{'X', 'X', 'O', 'X'},
							{'X', 'X', 'X', 'X'}};
	
		char [] [] board = {{'X', 'X', 'X', 'X'}, 
							{'X', 'O', 'O', 'X'},
							{'X', 'X', 'O', 'X'},
							{'X', 'X', 'O', 'X'}};

		
		char [] [] board = {{'X', 'X', 'X', 'X'}, 
							{'X', 'X', 'O', 'X'},
							{'X', 'O', 'O', 'X'},
							{'X', 'O', 'X', 'X'}};


		char [] [] board = {};
		*/
		
		char [][] board = {{'X', 'O', 'X', 'O', 'X', 'O'},
						   {'O', 'X', 'O', 'X', 'O', 'X'}, 
						   {'X', 'O', 'X', 'O', 'X', 'O'}, 
					       {'O', 'X', 'O', 'X', 'O', 'X'}};
		// expected: ["XOXOXO","OXXXXX","XXXXXO","OXOXOX"]
		
		
		
		/*
		String [] input = {"XOXOOOO","XOOOOOO","XOOOOXO","OOOOXOX","OXOOOOO","OOOOOOO","OXOOOOO"};
		// expected: ["XOXOOOO","XOOOOOO","XOOOOXO","OOOOXOX","OXOOOOO","OOOOOOO","OXOOOOO"]
		char [][] board = input2Board(input);
		*/
		
		SurroundedRegion solution = new SurroundedRegion();
		
		System.out.println("Input:");
		solution.printBoard(board);
		
		System.out.println("Output:");
		solution.solve(board);
		solution.printBoard(board);
		
	}


	private static char [][] input2Board(String [] input){
		
		char [][] res = new char[input.length][0];
		
		for(int i=0; i<input.length; i++){
			res[i] = input[i].toCharArray();
		}
		return res;
	}
	
}











