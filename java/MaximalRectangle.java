
/**
 * Given a 2D binary matrix filled with 0's and 1's, 
 * 	find the largest rectangle containing all ones and return its area.
 * 
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Jan 05, 2015
 *
 */
public class MaximalRectangle {

	private int maxArea(char[][] matrix, int i, int j){
		int row_len = matrix.length;
		int col_len = matrix[0].length;
		
		int area = 1; // starting point	
		for(int ma=i; ma<row_len && col_len > j; ++ma){
			int na = j;
			for(; na<col_len; ++na){
				if(matrix[ma][na] == '0'){
					//update the boundary of column
					col_len = na;
					break;
				}
			}
			// calculate the area of every possible rectangle
			area = Math.max(area, (ma-i+1) * (na-j));
		}
		return area;
	}
	
    public int maximalRectangle(char[][] matrix) {
    	int max_area = 0;
    	
    	for(int i=0; i<matrix.length; ++i){
    		for(int j=0; j<matrix[0].length; ++j){
    			if(matrix[i][j] == '1'){
    				//the max rectangle starting from this point
    				//  expanding to the right and bottom. 
    				max_area = Math.max(max_area, this.maxArea(matrix, i, j));
    			}
    		}
    	}
    	
    	return max_area;
    }
    
    
	public static void main(String[] args) {
		
		/**
		
		char [][] matrix = {
				{'1', '1', '0', '0', '0'},
				{'1', '1', '1', '0', '0'},
				{'0', '1', '1', '0', '0'},
				{'0', '1', '1', '1', '1'},
		}; // expect 6;
		*/
		
		
		//char [][] matrix = {"10","01","01","01","11","00","01"};
		
		String [] input = {
				 "11111111",
				 "11111110",
				 "11111110",
				 "11111000",
				 "01111000"
		}; // expect 21
		
		char [][] matrix = Utils.string2matrix(input);
		
		
		
		MaximalRectangle solution = new MaximalRectangle();
		System.out.println(solution.maximalRectangle(matrix));
	}

}










