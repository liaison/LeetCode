import static org.junit.Assert.*;

import org.junit.Test;



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

	public int candy_one_pass(int[] ratings) {
		int lastAscend = 0;
		// The baseline is that each child got at least one candy.
		int lastCandy = 1;
		int total = 1;

		for(int i=1; i<ratings.length; i++){

			if(ratings[i] > ratings[i-1]){
				lastAscend = i;
				lastCandy ++;
				total += lastCandy;

			}else if(ratings[i] == ratings[i-1]){
				lastAscend = i;

				/* A flat growth, two peers with the same rating might be given different candies.
				 * To minimize the number of candies, consecutive peers with the same rating
				 *  are given the minimal one candy for each.
				 * It might seem unfair that a peer right next to a ascending peek would be given
				 *  much more candies than its equivalent peers.
				 */
				lastCandy = 1;
				total += lastCandy;

			}else{
			    /*
			     *  This is a descending slope, since we give the minimal candy (1) up to this point,
			     *  we need to compensate the previous children, to make sure that they have one
			     *  more candy than the one next to them.
			     */
				if(lastCandy == 1){
					total += i - lastAscend;
				}

				/* When the slope starts to descend, reset the baseline to 1,
				*  instead of giving candy that is one less than the previous one (peak).
				*  to reduce the total number of candies that are given,
				*  yet it still meet the requirements.
				*/
				lastCandy = 1;
				total += lastCandy;
			}
		}

		return total;
    }

	@Test
	public void testCandy_one_pass() {
	    Candy candy = new Candy();

            int [] num1 = {1, 2, 4, 4, 3}; // expect 9;
            int [] num2 = {1, 2, 3, 4, 5}; // expect 15;
            int [] num3 = {5, 4, 3, 2, 1}; // expect 15;

            assertEquals(candy.candy(num1), 9);
            assertEquals(candy.candy(num2), 15);
            assertEquals(candy.candy(num3), 15);
	}

	private int slope(int n){
            return (1+n)*n/2;
	}

	/**
	 * https://oj.leetcode.com/discuss/13841/easy-understand-solution-with-comments-constant-space-pass
	 */
	public int candy(int[] ratings) {
		int up = 0, down = 0;
		int total = 0;
		int oldsign=0, newsign;

		for(int i=0; i<ratings.length-1; i++){

			newsign = (ratings[i] < ratings[i+1]) ? 1:
					  (ratings[i] > ratings[i+1]) ? -1: 0;

			if((oldsign > 0 && newsign == 0) ||
			   (oldsign < 0 && newsign >= 0)){

				total += slope(up) + slope(down) + Math.max(up, down);
				up = 0;
				down = 0;
			}

			if(newsign > 0){
				up ++;

			}else if(newsign < 0){
				down++;

			}else{
				total += 1;
			}

			oldsign = newsign;
		}

		total += slope(up) + slope(down) + Math.max(up, down)+1;

		return total;
	}

	/**
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
	*/


	public static void main(String[] args) {
		//int [] num = {8, 7, 1, 4, 5, 2};  // expect 12
		//int [] num = {1,3,4,3,2,1};	// expect 13

		//int [] num = {2, 2};  // expect 2;

		//int [] num = {1, 2, 2};  // expect 4;

		//int [] num = {2, 2, 1};  // expect 4;

		//int [] num = {1, 2, 4, 4, 3}; // expect 9;
		int [] num = {1, 2, 3, 4, 5}; // expect 15;
		//int [] num = {5, 4, 3, 2, 1}; // expect 15;


		Candy solution = new Candy();

		System.out.println(solution.candy(num));
	}

}





