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
		int res = 0;
		int i = 0, count = gas.length;
		while(count > 0) {
			if(gas[i] - cost[i] > max_gas_left) {
				max_gas_left = gas[i] - cost[i];
				res = i;
			}
			i = (i+1) % gas.length;
			-- count;
		}
		
		return res;
	}
	
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int length = gas.length;
        int start = bestStartPoint(gas, cost);
        
        //System.out.println("Best Start Point:" + start);
        
        int i = start, count = gas.length;
		while(count > 0) {
			if(canReach(i, (i+1) % length, 0, gas, cost)) {
        		return i;
        	}
			i = (i+1) % length;
			-- count;
        }
        return -1;
    }
    
    
	public static void main(String[] args) {
		int gas[]  = {8, 20, 15};
		int cost[] = {10, 17, 9};
		
		GasStation solution = new GasStation();
		System.out.println(solution.canCompleteCircuit(gas, cost));
	}

}







