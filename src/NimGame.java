
/**
 * https://leetcode.com/problems/nim-game/
 * 
 * You are playing the following Nim Game with your friend: 
 * There is a heap of stones on the table, each time one of you take turns to 
 * remove 1 to 3 stones. The one who removes the last stone will be the winner.
 * You will take the first turn to remove the stones.
 * 
 * Both of you are very clever and have optimal strategies for the game. 
 * Write a function to determine whether you can win the game given the number
 *  of stones in the heap.
 *  
 *  For example, if there are 4 stones in the heap, then you will never win 
 *  the game: no matter 1, 2, or 3 stones you remove, the last stone will 
 *  always be removed by your friend.
 */

import static org.junit.Assert.*;
import org.junit.Test;


public class NimGame {

	/**
	 * Theorem: The first one who got the number that is mod of 4 will lost. 
	 * 
	 * For any number that is greater that 4, the first one who can reduce the
	 *  the number into mod of 4 will eventually win, since it would leave the 
	 *  other player to pick from the number of mod 4.
	 * 
	 * Special cases: for num < 4, the first one pick will win the game.
	 */
    public boolean canWinNim(int n) {    
        return n % 4 != 0 ;
    }

    @Test
    public void testCanWinNim() {
    	int n = 8;
    	NimGame ng = new NimGame();
    	
    	assertFalse(ng.canWinNim(n));
    }
}
