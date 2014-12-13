import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;


/**
 * 
 * 
 *	Given a collection of intervals, merge all overlapping intervals.

	For example,
	Given [1,3],[2,6],[8,10],[15,18],
	return [1,6],[8,10],[15,18].
 * 
 * @author Lisong Guo <lisong.guo@inria.fr>
 *
 */
public class MergeIntervals {

	private LinkedList<Interval> addInterval(LinkedList<Interval> list, Interval i){

		for(Interval range : list){
			
			// 				|------|
			//   |=======|
			if(i.start > range.end){
				// check next range
				continue;
			}
			
			// identical interval, skip this one.
			if(i.start == range.start && i.end == range.end){
				return list;
			
			// |------|
			//     |=======|
			}else if(i.start <= range.start && i.end >= range.start && i.end <= range.end){
				// merge
				list.remove(range);
				range.start = i.start;
				return addInterval(list, range);
			
			//          |------|
			//     |=======|
			}else if(i.start >= range.start && i.start <= range.end && i.end >= range.end){
				// merge 
				list.remove(range);
				range.end = i.end;
				return addInterval(list, range);
			
			//    |----| 
			//  |=========|
			}else if(i.start >= range.start && i.end <= range.end){
				// ignore this new interval
				return list;
			
			// |--------------|
			//     |====|
			}else if(i.start <= range.start && i.end >= range.end){
				// replace the head with the new interval
				list.remove(range);
				range.start = i.start;
				range.end = i.end;
				return addInterval(list, range);
			
			// 	|------|
			//    		 |====|	
			}else if(i.end < range.start){
				// add before the current range 
				list.add(list.indexOf(range), i);
				return list;
			}
		
		}
		
		
		// The new interval is even further than any current interval, 
		//	then add it to the tail. 
		list.addLast(i);
		
		return list;
		
	}

	/**
    public List<Interval> merge(List<Interval> intervals) {
    	
    	LinkedList<Interval> result = new LinkedList<Interval>();
    	for(Interval iter : intervals){
    		// recursively add a new interval to the list, 
    		//	in sort of the "insertion_sort" manner.
    		result = addInterval(result, iter);
    	}
    	return result;
    }
    */
	
	public List<Interval> merge(List<Interval> intervals){
		LinkedList<Interval> result = new LinkedList<Interval>();
		
		if(intervals.isEmpty()){
			return result;
		}
		
		Collections.sort(intervals, new IntervalComparator());
		int l=intervals.get(0).start, r=intervals.get(0).end;
		
		for(Interval iter : intervals){
			if(iter.start <= r){
				r = Math.max(iter.end, r);
			}else{
				result.add(new Interval(l,r));
				l = iter.start;
				r = iter.end;
			}
		}
		result.add(new Interval(l, r));
		
		return result;
	}

	
	class IntervalComparator implements Comparator<Interval> {
	    @Override
	    public int compare(Interval a, Interval b) {
	        if(a.start < b.start){
	        	return -1;
	        }else if(a.start == b.start){
	        	return 0;
	        }else{
	        	return 1;
	        }
	    }
	}

	/**
	 * 
		Given a set of non-overlapping intervals, 
			insert a new interval into the intervals (merge if necessary).

		You may assume that the intervals were initially sorted according to their start times.

		Example 1:
			Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

		Example 2:
			Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

			This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
	 */
	
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
    	intervals.add(newInterval);
    	LinkedList<Interval> newResult = new LinkedList<Interval>();
    	
    	Collections.sort(intervals, new IntervalComparator());
    	int start = intervals.get(0).start;
    	int end = intervals.get(0).end;
    	
    	for(Interval i : intervals){
    		if(i.start <= end){
    			end = Math.max(end, i.end);
    			continue;
    		}else{
    			newResult.add(new Interval(start, end));
    			start = i.start;
    			end = i.end;
    		}
    	}
    	
    	newResult.add(new Interval(start, end));
    	
    	return newResult;
    }
    
    
    private static List<Interval> getIntervalList(int [] input){
    	LinkedList<Interval> result = new LinkedList<Interval>();
    	
    	for(int i=0; i< input.length; i+=2){
    		Interval newInterval = new Interval(input[i], input[i+1]);
    		result.addLast(newInterval);
    	}
    	
    	return result;
    }
    
    
    
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int input [] = {1,3,	2,6,	8,10,	15,18};
		
		//int input [] = {1,4,	1,4};  // expected result {1, 4}
		
		//int input [] = {1,4,	1,5};  // expected result {1, 5}
		
		//int input [] = {1,4, 	0,2};  // expected result {0, 4}
		
		//int input [] = {1,4, 	0,0};  // expected result {0, 0,  1, 4}
		
		// expecte result  [[0,0],[2,3],[4,7]]
		//int input [] = {0,0,  4,5,	5,6, 5,5,  2,3,  5,7,  0,0};
		
		MergeIntervals solution = new MergeIntervals();
		
		List<Interval> result = solution.merge(getIntervalList(input));

		Utils.printIntervalList(result);
		
		
		//int input2 [] = {1,3,  6,9};  Interval newInterval = new Interval(2,5);
		//int input2 [] = {1,2, 3,5, 6,7,	8,10, 12,16};
		//Interval newInterval = new Interval(4,9);
		int input2 [] = {1,5};
		Interval newInterval = new Interval(5, 7);
		
		List<Interval> input2_list = getIntervalList(input2);
		List<Interval> input2_res = 
				solution.insert(input2_list, newInterval);
		Utils.printIntervalList(input2_res);
	}

}












