import static org.junit.Assert.*;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Arrays;
import java.util.Vector;

import org.junit.Test;


public class CountInversion {
	
	private Vector<Integer> nums = new Vector<Integer>();
	
	public void loadTestInput() {
		nums.clear();
		
		Integer [] array = {1, 3, 2};
		nums.addAll(Arrays.asList(array));	
	}
	
	
	public void loadRealInput() {

		try{	
			FileReader inputFile = new FileReader("input/IntegerArray.txt");
			BufferedReader input = new BufferedReader(inputFile);
			
			String line = input.readLine(); 
			while(line != null) {
				this.nums.add(Integer.valueOf(line));
				line = input.readLine();
			}
			
			System.out.println("input size:" + this.nums.size());
			
			input.close();
			
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	public long merge_count(Vector<Integer> left,
							Vector<Integer> right,
							Vector<Integer> result) {
		int i = 0, j = 0, k = 0;
		long count = 0;
		int total = left.size() + right.size();
		
		result.clear();
		
		while(k < total) {
			if(i >= left.size() ) {
				result.add(right.get(j));
				++j;
			
			} else if( j >= right.size() ) {
				result.add(left.get(i));
				++i;
				
			} else if(left.get(i) > right.get(j)) {
				
				result.add(right.get(j));
				count += (left.size() - i);
				++j;
				
			} else {
				result.add(left.get(i));
				++i;
			}
			++k;
		}
		
		return count;
	}
	
	public long countInversionMergeSort() {
		Vector<Integer> output = new Vector<Integer>();
		
		return countInversionMergeSort(this.nums, output);
	}
	
	protected long countInversionMergeSort(
		Vector<Integer> input,
		Vector<Integer> output) {
		
		if(input.size() == 0 || input.size() == 1) {
			output.addAll(input);
			return 0;	
		}
		
		int pival = input.size() / 2;
		
		Vector<Integer> left = new Vector<Integer>();
		left.addAll(input.subList(0, pival));
		
		Vector<Integer> right = new Vector<Integer>();
		right.addAll(input.subList(pival, input.size()));
		
		Vector<Integer> leftResult = new Vector<Integer>();
		Vector<Integer> rightResult = new Vector<Integer>();
		
		long leftCount  = countInversionMergeSort(left, leftResult);
		long rightCount = countInversionMergeSort(right, rightResult);
		
		long mergeCount = merge_count(leftResult, rightResult, output);
		
		return (leftCount + rightCount + mergeCount);
	}
	
	public long countInversionNaive() {
		int n = nums.size();
		long count = 0;
		
		for(int i=0; i<n; ++i) {
			for(int j=i+1; j<n; ++j) {
				if(nums.get(i) > nums.get(j)){
					count ++;
				}
			}
		}
		
		return count;
	}
	
	public void addElement(Vector<Integer> input) {
		input.addElement(1);
	}
	
	//@Test
	public void testVector() {
		
		CountInversion ci = new CountInversion();
		
		Vector<Integer> input = new Vector<Integer>();
		
		ci.addElement(input);
		
		System.out.println(input.size());
	}
	
	
	@Test
	public void testCountInversionMergeSort() {
		
		CountInversion ci = new CountInversion();
		
		//ci.loadTestInput();
		//assertEquals(1, ci.countInversionMergeSort());
			
		ci.loadRealInput();
		System.out.println(ci.countInversionMergeSort());
		
	}
	
	
	//@Test
	public void testCountInversionNaive() {
		CountInversion ci = new CountInversion();
		
		ci.loadRealInput();
		System.out.println(ci.countInversionNaive());
		
		/*
		ci.loadTestInput();
		assertEquals(1, ci.countInversion());
		*/
	}
}











