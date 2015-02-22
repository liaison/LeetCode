/**
 * Given two integers n and k, 
   return all possible combinations of k numbers out of 1 ... n.

	For example,
		If n = 4 and k = 2, a solution is:

		[
  			[2,4],
  			[3,4],
  			[2,3],
  			[1,2],
  			[1,3],
  			[1,4],
		]

 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Feb 23, 2015
 *
 */
import java.util.Arrays;
import java.util.List;
import java.util.LinkedList;
import java.util.ArrayList;

public class Combination {
	
	private List<List<Integer>> res = new LinkedList<List<Integer>>();
	private int k, n;
	
	private void combine_rec(int index, Integer [] vec, int start) {
		// Reach a combination
		if (index == this.k) {
			ArrayList<Integer> newComb = new ArrayList<Integer>();
			for (Integer v : vec) {
				newComb.add(v);
			}
			this.res.add(newComb);
			return;
		}
		
		for (int i=start; i<=this.n; ++i) {
			vec[index] = i;
			combine_rec(index+1, vec, i+1);
		}
	}
	
	public List<List<Integer>> combine(int n, int k) {
		Integer[] vec = new Integer[k];
		this.k = k;
		this.n = n;
		combine_rec(0, vec, 1);
		return res;
    }
    
    
	public static void main(String[] args) {
		Combination solution = new Combination();
		int n = 4, k = 1;
		
		Utils.printListOfList(solution.combine(n, k));
	}

}






