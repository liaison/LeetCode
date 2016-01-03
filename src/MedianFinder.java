import java.util.Comparator;
import java.util.PriorityQueue;

//import java.util.TreeSet;


/**
 * Return the median of the data stream.
 * 
 * mid = size / 2
 * 
 * If size(data_stream) % 2 == 1 then
 *     median = data_stream[mid]
 * If size(data_stream) % 2 == 0 then
 *     median = data_stream[mid-1] + data_stream[mid]
 *
 */
class MedianFinder {

	class Descend implements Comparator<Integer>
	{	
		public int compare(Integer A, Integer B) {
			return B - A;
		}
	}

	private PriorityQueue<Integer> firstHalf =
			new PriorityQueue<Integer>(1000, new Descend());
	
	private PriorityQueue<Integer> secondHalf = new PriorityQueue<Integer>();
	private double median = Double.MAX_VALUE;

	
    // Adds a number into the data structure.
    public void addNum(int num) {
        if(num < median) {
        	firstHalf.add(num);
        } else {
        	secondHalf.add(num);
        }
        
        updateMedian();
    }

    private void updateMedian() {
    	int firstHalfSize = firstHalf.size();
    	int secondHalfSize = secondHalf.size();

    	// re-balancing
    	if(firstHalfSize == secondHalfSize) {
    		median = (firstHalf.peek() + secondHalf.peek())/2.0;	
    	
    	} else if(firstHalfSize > secondHalfSize) {
			if(firstHalfSize - secondHalfSize == 1) {
				median = firstHalf.peek();
			} else {
				int last_firstHalf = firstHalf.poll();
				secondHalf.offer(last_firstHalf);
				updateMedian();
			}
		
    	} else if (firstHalfSize < secondHalfSize) {
			if(secondHalfSize - firstHalfSize == 1) {
				median = secondHalf.peek();
			} else {
				int first_secondHalf = secondHalf.poll();
				firstHalf.offer(first_secondHalf);
				updateMedian();
			}
		}
    }

    // Returns the median of current data stream
    public double findMedian() {
        return median;
    }

	public void addList(int [] list) {
		for(int num : list) {
			this.addNum(num);
		}
	}

    public static void main(String[] args) {
    	
    	MedianFinder mf = new MedianFinder();
    	/*
    	[6.00000,
    	 8.00000,
    	 6.00000,
    	 6.00000,
    	 6.00000,
    	 5.50000,
    	 6.00000,
    	 5.50000,
    	 5.00000,
    	 4.00000,
    	 3.00000]
    			
    	addNum(6),findMedian(),
    	addNum(10),findMedian(),
    	addNum(2),findMedian(),
    	addNum(6),findMedian(),
    	addNum(5),findMedian(),
    	addNum(0),findMedian(),
    	addNum(6),findMedian(),
    	addNum(3),findMedian(),
    	addNum(1),findMedian(),
    	addNum(0),findMedian(),
    	addNum(0),findMedian()
    	
    	*/
    	
    	int [] nums = {6, 10, 2, 6, 5, 0};
		
    	mf.addList(nums);
    	
    	System.out.println(mf.findMedian());
	}
	
};



