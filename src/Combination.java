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
import static org.junit.Assert.*;

import java.util.List;
import java.util.LinkedList;
import java.util.ArrayList;

import org.junit.Test;

public class Combination {

	private List<List<Integer>> res = new LinkedList<List<Integer>>();
	private int k, n;

	/**
	 *
	 * Enumerate the combination of numbers and fill the resulting combination
	 *   in a recursive way.
	 *
	 * @param index: the index of element to be filled in the resulting vector.
	 * @param vec:   the original vector that contains all the numbers.
	 * @param start: the starting point in the "vec" to be considered as candidates.
	 *
	 */
	private void combine_rec(int index, Integer [] vec, int start) {
		// Reach a combination
		if (index == this.k) {
		    // Clone the result vector
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
	    res.clear();

		Integer[] vec = new Integer[k];
		this.k = k;
		this.n = n;
		combine_rec(0, vec, 1);
		return res;
    }

	@Test
	public void testCombine_case_1() {
	    Combination com = new Combination();
	    List<List<Integer>> res = com.combine(4, 2);

	    /**
	     * Expected result:
	     * [1, 2]
           [1, 3]
           [1, 4]
           [2, 3]
           [2, 4]
           [3, 4]
	     */
	    assertEquals(6, res.size());
	}

    @Test
    public void testCombine_case_2() {
        Combination com = new Combination();
        List<List<Integer>> res = com.combine(4, 1);

        /**
         * Expected result:
         * [1]
           [2]
           [3]
           [4]
         */
        assertEquals(4, res.size());
    }


	public static void main(String[] args) {
		Combination solution = new Combination();
		int n = 4, k = 2;

		Utils.printListOfList(solution.combine(n, k));
	}

}






