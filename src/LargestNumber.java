/**
 * 
Given a list of non negative integers, 
	arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, 
	so you need to return a string instead of an integer.

 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Jan 13, 2015
 *
 */
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class LargestNumber {

	class NumberComparator implements Comparator<String> {
	    @Override
	    public int compare(String a, String b) {
	        int al = a.length();
	        int bl = b.length();
	    	int i = 0;
	    	while(i<al && i<bl){
	    		if(a.charAt(i) > b.charAt(i)){
	    			return 1;
	    		}else if(a.charAt(i) < b.charAt(i)){
	    			return -1;
	    		}
	    		// a.charAt(i) == b.charAt(i)
	    		++i;
	    	}
	    	
	    	if(al == bl){
	    		return 0;
	    	}else if(al < bl){
	    		return compare(a, b.substring(i));
	    	}else{
	    		return compare(a.substring(i), b);
	    	}
	    }
	}
	
	public String largestNumber(int[] num) {
		ArrayList<String> nums = new ArrayList<String>();
		for(int i : num){
			nums.add(String.valueOf(i));
		}
		
		Collections.sort(nums, new NumberComparator());
		
		StringBuffer res = new StringBuffer();
		
		for(int i=nums.size()-1; i>=0; --i){
			res.append(nums.get(i));
		}
		
		// if all zeros, then return only a single zero
		if(res.length() > 0 && res.charAt(0) == '0'){
			return "0";
		}else{
			return res.toString();
		}
	}
    
    
    public static void main(String[] args) {
    	int [] num = {30, 3, 34, 9, 5};  // expected 9 5 34 3 30
    	//int [] num = {0, 0};               // expected 0, instead of 00
    	//int [] num = {824,938,1399,5607,6973,5703,9609,4398,8247};
    		// expected "9609 938 824 8247 6973 5703 5607 4398 1399"
    	
    	LargestNumber solution = new LargestNumber();
    	System.out.println(solution.largestNumber(num));
    }

}
