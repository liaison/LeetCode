

/**
 * 
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

	Each child must have at least one candy.
	Children with a higher rating get more candies than their neighbors.
	What is the minimum candies you must give?


 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Dec 27, 2014
 *
 */
public class Candy {
    
	/**
	public int candy(int[] ratings) {
		int lastAscend = 0;
		int lastCandy = 1;
		int total = 1;
		
		for(int i=1; i<ratings.length; i++){
			if(ratings[i] > ratings[i-1]){
				lastAscend = i;
				lastCandy ++;
				total += lastCandy;
			
			}else if(ratings[i] == ratings[i-1]){
				lastAscend = i;
				lastCandy = 1;
				total += lastCandy;
			
			}else{
				if(lastCandy == 1){
					total += i - lastAscend;
				}

				lastCandy = 1;	
				total += lastCandy;
			}
		}
		
		return total;
    }
    */
	
	/**
	public int candy(int[] ratings) {
		int [] candys = new int[ratings.length];
		candys[0] = 1;
		int total = candys[0];
		
		for(int i=1; i<ratings.length; i++){
			
			if(ratings[i] > ratings[i-1]){
				candys[i] = candys[i-1] + 1;
			
			}else if(ratings[i] == ratings[i-1]){
				candys[i] = 1;
			
			}else{
				candys[i] = 1;
				int j = i - 1;
				while(j >= 0){
					if(ratings[j] > ratings[j+1] && 
					    candys[j] <= ratings[j+1]){
						candys[j] ++;
						total ++;
						
					}else{
						break;
					}				
					j --;
				}
			}
			
			total += candys[i];
		}
		
		return total;
	}
	*/
	public int candy(int[] ratings) {
		int [] candys = new int[ratings.length];
		int total = 0;
		
		candys[0] = 1;
		for(int i=1; i<ratings.length; i++){
			
			if(ratings[i] > ratings[i-1]){
				candys[i] = candys[i-1] + 1;
			}else{
				candys[i] = 1;
			}
		}
		
		for(int i=ratings.length-1; i>0; i--){
			if(ratings[i-1] > ratings[i]){
				candys[i-1] = Math.max(candys[i] + 1, candys[i-1]);
			}
		}
		
		for(int i=0; i<candys.length; i++){
			total += candys[i];
		}
		
		return total;
	}
	
	
	
	public static void main(String[] args) {
		//int [] num = {8, 7, 1, 4, 5, 2};  // expect 12
		//int [] num = {1,3,4,3,2,1};	// expect 13
		
		//int [] num = {2, 2};  // expect 2;
		
		//int [] num = {1, 2, 2};  // expect 4;
		
		//int [] num = {2, 2, 1};  // expect 4;
		
		int [] num = {1, 2, 3, 4, 5}; // expect 15;
		//int [] num = {5, 4, 3, 2, 1}; // expect 15;
		
		
		Candy solution = new Candy();
		
		System.out.println(solution.candy(num));
	}

}





