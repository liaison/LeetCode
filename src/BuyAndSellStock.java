
/**
 * Say you have an array for which the ith element is the price of a given stock on day i.

	If you were only permitted to complete at most one transaction 
	(ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
 * 
 * @author Lisong Guo <lisong.guo@inria.fr>
 * @date   Nov 08, 2014
 */

public class BuyAndSellStock {

	/**
	 * One can only have one transaction, one buy and one sell, 
	 * 	but the transaction can happen on the same day.
	 * 
	 * @return
	 */
	public int maxProfit(int[] prices) {
    
		if(prices.length <= 1){
			return 0;
		}
		
		int curLow = prices[0];
		int maxProfit = Integer.MIN_VALUE;
		
		for(int i=1; i<prices.length; i++){
			int newProfit = prices[i] - curLow;
			
			maxProfit = (maxProfit < newProfit) ? newProfit : maxProfit;
			
			if(prices[i] < curLow){
				curLow = prices[i];
			}
		}
		
		// In the worst case, buy and sell the stock on the same day.
		return maxProfit < 0 ? 0 : maxProfit;
    }
	
	
	/**
	 * One can have as many transactions as possible to maximize the profits.
	 * @return
	 */
	public int maxProfitMultiTrans(int [] prices){
		if(prices.length <= 1){
			return 0;
		}
		
		
		return 0;
	}
	
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		//int [] prices = {5, 4, 3, 2, 1};
		int [] prices = {2, 1};  // expect 0 
		
		BuyAndSellStock solution = new BuyAndSellStock();
		
		System.out.println(solution.maxProfit(prices));
		
	}

}






