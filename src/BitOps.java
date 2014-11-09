

/**
 * 
 * All the problems that involve bit operations.
 *  
 * @author Lisong Guo <lisong.guo@inria.fr>
 * @date   Nov 09, 2014
 *
 */
public class BitOps {
	
	
	/**
	 *	Implement int sqrt(int x).
   	 *	Compute and return the square root of x.
     *  Note: the tag of this problem suggests "binary search". 
	 * 
	 * This solution would exceed the time limit.
	 */
	public int sqrt(int x) {
		int mid = 0;
		int low = 0, high = x;
		
		while(low < high - 1){
			mid = (low + high) >> 1;
			int mid_power = mid * mid;
			if(mid_power < x){
				low = mid;
			}else if(mid_power > x){
				high = mid;
			}else{
				return mid;
			}
		}
		// approximation 
		return low;
    }
	
	/**
	 * The time complexity of this solution is O(1), i.e. 15 times of iteration.
	 * https://oj.leetcode.com/discuss/8897/share-my-o-log-n-solution-using-bit-manipulation
	 */
	public int bsqrt(int x){
		long ans = 0;
		long bit = 1l << 16;
		
		while(bit > 0){
			ans |= bit;	
			if(ans * ans > x){
				// revert the current bit from 1 to 0, 
				//	and preserve the high bits in the result.
				ans ^= bit;
			}
			bit >>= 1;
		}
		
		return (int)ans;
	}
	

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int x = 8;
		BitOps solution = new BitOps();
		
		long startTime = System.currentTimeMillis();
		
		System.out.println(solution.bsqrt(x));
	
		long endTime = System.currentTimeMillis();
		long elapsedTime = endTime - startTime;
		
		System.out.println("Time: " + elapsedTime);
	}

}




