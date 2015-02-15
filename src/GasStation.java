/**
 * 
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Feb 15, 2015
 *
 *
 * There are N gas stations along a circular route, 
 * 	where the amount of gas at station i is gas[i].

	You have a car with an unlimited gas tank and it costs cost[i] of gas to travel 
		from station i to its next station (i+1). 
	You begin the journey with an empty tank at one of the gas stations.

	Return the starting gas station's index if you can travel around the circuit once, 
		otherwise return -1.

	Note:
		The solution is guaranteed to be unique.
    Tag: 
    	Greedy
 */
public class GasStation {

	private boolean canReach(int start, int next, int tank, 
							 int[] gas, int[] cost) {
		// return to the start point.
		if(start == next) return true; 
		
		int length = gas.length;
		int pre = next == 0 ? length-1 : next - 1;
		
		tank = tank + gas[pre] - cost[pre];
		if(tank < 0) 
			// not possible to reach the next station.
			return false; 
		else
			// carry on 
			return canReach(start, (next+1) % length, tank, gas, cost); 
	}
	
	
	private int bestStartPoint(int[] gas, int[] cost) {
		int max_gas_left = Integer.MIN_VALUE;
		int i = 0, count = gas.length;
		int res = -1;
		
		int tank = 0;
		int left = 0;
		
		while(count > 0) {
			left = gas[i] - cost[i];
			if(left > max_gas_left) {
				max_gas_left = left;
				res = i;
			}
			tank += left;
			i = (i+1) % gas.length;
			-- count;
		}
		
		return tank < 0 ? -1 : res;
	}
	
	
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int length = gas.length;
        int res = -1;
        
        int i = this.bestStartPoint(gas, cost);
        if(i == -1) return -1;
        
        int count = gas.length;
		while(count > 0) {
			if(this.canReach(i, (i+1)%length, 0, gas, cost)){
				return i;
			}
			i = (i+1) % length;
			-- count;
        }
        return res;
    }
    
    
	public static void main(String[] args) {
		int gas[]  = {6,1,4,3,5};
		int cost[] = {3,8,2,4,2};  // expected 2;
		
		GasStation solution = new GasStation();
		System.out.println(solution.canCompleteCircuit(gas, cost));
	}

}







