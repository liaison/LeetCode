/**
 * 
   Write an efficient algorithm that searches for a value in an m x n matrix. 
   This matrix has the following properties:

	Integers in each row are sorted from left to right.
	The first integer of each row is greater than the last integer of the previous row.
	
	For example,

	Consider the following matrix:

	[
  		[1,   3,  5,  7],
  		[10, 11, 16, 20],
  		[23, 30, 34, 50]
	]
	Given target = 3, return true.

 * @author Lisong Guo <lisong.guo@inria.fr>
 * @date   Nov 06, 2014
 *
 */
public class MatrixSearch {

	/**
	 *  Do binary search in this "ordered" matrix
	 * @return
	 */
	public boolean searchMatrix(int[][] matrix, int target) {
		
		int row_num = matrix.length;
		int col_num = matrix[0].length;
		
		int begin = 0, end = row_num * col_num - 1;
		
		while(begin < end){
			int mid = (begin + end) / 2;
			
			if(matrix[mid/col_num][mid%col_num] == target){
				return true;
			
			}else if(matrix[mid/col_num][mid%col_num] < target){
				//Should move a bit further, otherwise dead loop.
				begin = mid+1;
			}else{
				end = mid;
			}
		}
		
		// Deal with the input {{1}} when begin == end
		if(matrix[begin/col_num][begin%col_num] == target){
			return true;
		}else{	
			return false;
		}
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		MatrixSearch ms = new MatrixSearch();
		
		/**
		int [][] matrix = 
			{
				{1,   3,  5,  7},
	  			{10, 11, 16, 20},
	  			{23, 30, 34, 50} 
	  		};
		*/
		
		int [] [] matrix = {{1}};
		
		System.out.println(ms.searchMatrix(matrix, 3));
		
	}

}



















