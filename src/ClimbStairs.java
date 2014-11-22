
/**
 * 
 * 
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. 

In how many distinct ways can you climb to the top?

 * @author Lisong Guo <lisong.guo@inria.fr>
 * @date   Nov 22, 2014
 *
 */
public class ClimbStairs {

	/**
	 * 1 2 
	 * 1 2 3 
	 * 1 2 3 5 
	 * @param n
	 * @return
	 */
    public int climbStairs(int n) {
        if(n <= 0) return 0;
        
        if(n == 1) return 1;
        if(n == 2) return 2;
        
        int one_step_before = 1;
        int two_steps_before = 2;
        int all_ways = 0;
        
        for(int i=2; i<n; i++){
        	all_ways = one_step_before + two_steps_before;
        	one_step_before = two_steps_before;
        	two_steps_before = all_ways;
        }
        return all_ways;
    }
    
	/**
	 * @param args
	 */
	public static void main(String[] args) {

		int n = 4; 
		ClimbStairs solution = new ClimbStairs();
		
		System.out.println(solution.climbStairs(n));
	}

}




