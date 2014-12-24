import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;


/**
 * 
 * 

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, 
	where 'Q' and '.' both indicate a queen and an empty space respectively.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement,
 where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

 * @author Lisong Guo<lisong.guo@me.com>
 * @date   Dec 24, 2014
 *
 */
public class NQueen {

	private int N;	
	private boolean [] stripMap  = null;
	private boolean [] columnMap = null;
	
	// The column position of each queue for each row. 
	//  The index of colPosition is also the row index, 
	//   and the value at the index is the column index. 
	private int [] colPosition = null;
	
	private boolean needOutput = false;
	private int totalCount = 0;
	private LinkedList<String []> res = new LinkedList<String []>();
	
    public List<String[]> solveNQueens(int n) {
    	this.N = n;
    	this.stripMap = new boolean[4*this.N];
    	this.columnMap = new boolean[this.N];
    	this.colPosition = new int[this.N+1];
    	this.needOutput = true;
    	this.totalCount = 0;
    	
    	backtrack(0, 0);
    	return res;
    }
    
    public int totalNQueens(int n) {
    	this.N = n;
    	this.stripMap = new boolean[4*this.N];
    	this.columnMap = new boolean[this.N];
    	this.colPosition = new int[this.N+1];
    	this.totalCount = 0;
    	
    	backtrack(0, 0);
    	return this.totalCount;
    }
    
	private void backtrack(int curRow, int count){
		if(count == N){
			if(needOutput)
				addResult();
			
			totalCount ++;
			return;
		}
		
		for(int col=0; col<N; col++){
			if(isSafe(curRow, col)){
				placeQueue(curRow, col);
				backtrack(curRow+1, count+1);
				// remove this candidate, try another one
				removeQueue(curRow, col);
			}
		}
	}
	
	private boolean isSafe(int row, int col){
		// check whether it is safe along the column
		if(columnMap[col]){
			return false;
		}
		
		// check whether it is safe along the strips in two directions.
		if(stripMap[row+col] || stripMap[row + (N-col) + 2*N-2]){
			return false;
		}
		
		return true;
	}
	
	private void placeQueue(int row, int col){
		// marker the strip in the north-east direction.
		// Pattern: the cells laying in the same strip 
		//	share the same values of (row+col) and row+(N-col).
		// Assume the indice of rows start from top to bottom, 
		//  and the indice of columns start from left to right. 
		stripMap[row+col] = true;
		stripMap[row+(N-col) + 2*N-2] = true;
		
		columnMap[col] = true;
		
		// add a queue to the row at the specific column.
		colPosition[row] = col;
	}
	
	private void removeQueue(int row, int col){
		// remove the place marker.
		stripMap[row+col] = false;
		stripMap[row+(N-col) + 2*N-2] = false;
		
		columnMap[col] = false;
	}
	
	
	
	private void addResult(){
		String [] newSchema = new String[this.N];
		StringBuffer rowStr = new StringBuffer(this.N);
		
		for(int row=0; row<this.N; row++){		
			for(int c=0; c<this.N; c++){
				if(c == colPosition[row]){
					rowStr.append('Q');
				}else{
					rowStr.append('.');
				}
			}
			newSchema[row] = rowStr.toString();
			rowStr.delete(0, this.N);
		}
		this.res.add(newSchema);
	}
	
	
	public static void main(String[] args) {
		NQueen solution = new NQueen();
		
		int n = 4;
		
		Utils.printListOfStringArray(solution.solveNQueens(n));
		
		System.out.println(solution.totalNQueens(n));
	}

}
