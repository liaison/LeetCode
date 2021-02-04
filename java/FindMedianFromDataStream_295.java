import java.util.Collections;
import java.util.PriorityQueue;

class FindMedianFromDataStream_295 {

    private PriorityQueue<Integer> lowHalf;
    private PriorityQueue<Integer> highHalf;

    /** initialize your data structure here. */
    public MedianFinder() {
        // the size of lowHalf would be equal or greater than the highHalf
        lowHalf = new PriorityQueue<>(10, Collections.reverseOrder());
        highHalf = new PriorityQueue<>(10);
    }

    public void addNum(int num) {
        // Add the new element to the two heaps
        // always starts from the lower half
        lowHalf.add(num);
        highHalf.add(lowHalf.poll());

        // rebalance out the two heaps if necessary,
        // to make the size of lowHalf equal or great than highHalf
        if (lowHalf.size() < highHalf.size()) {
            lowHalf.add(highHalf.poll());
        }
    }

    public double findMedian() {
        if (lowHalf.size() == highHalf.size()) {
            // half and half
            return (lowHalf.peek() + highHalf.peek()) / 2.0;
        } else {
            // the top of the lowHalf would be the median
            return lowHalf.peek();
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */