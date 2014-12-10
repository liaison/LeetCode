import java.util.Stack;



/**
 * 

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Dec 10, 2014
 *
 */

public class MinStack {
	
	/*
	class ListNode {
		int val;
		int so_far_min;
		ListNode next;
		
		ListNode(int x) {
			val = x;
			next = null;
		}
	}
	
	private ListNode head = null;
	
    public void push(int x) {
        
        if(head == null){
        	head = new ListNode(x);
        	head.so_far_min = x;
        }else{
        	ListNode newNode = new ListNode(x);
        	newNode.so_far_min = Math.min(head.so_far_min, x);
        	newNode.next = head;
        	head = newNode;    	
        }
    }

    public void pop() {
        if(head != null){
        	head = head.next;
        }
    }

    public int top() {
        if(head != null){
        	return head.val;
        }else{
        	return -1; // ?, should throw exception here. 
        }
    }

    public int getMin() {
    	if(head != null){
    		return head.so_far_min;
    	}else{
    		// ?, again, should have some specific error code or exception here.
    		return -1;
    	}
    }
    */
    
 
	/**
	 * A smart solution inspired by
	 * https://oj.leetcode.com/discuss/15679/share-my-java-solution-with-only-one-stack
	 * 
	 */
	// the value would overflow/underflow, so need to store the long instead of integer
	Stack<Long> diffStack = new Stack<Long>();
	private long min_value = 0;
	
    public void push(int x) {
    	if(diffStack.isEmpty())
    		this.min_value = x;
    	
        diffStack.push(x-min_value);
        if(x < min_value)
        	min_value = x;
    }

    public void pop() {
    	if(diffStack.isEmpty())
    		return;
    	
    	long top = diffStack.pop();
    	if(top < 0){
    		// recover the previous min value
    		min_value = min_value - top;
    	}
    	
    }

    public int top() {
        long top = diffStack.peek();
        long res;
        
        if(top < 0){
        	res = min_value;
        }else{
        	res = min_value + top;
        }
        
        return (int)res;
    }

    public int getMin() {
    	return (int)this.min_value;
    }
    
    
    
	public static void main(String[] args) {
		MinStack mystack = new MinStack();
		
		//	push(2),push(0),push(3),push(0),getMin,pop,getMin,pop,getMin,pop,getMin, expected: 	[0,0,0,2]
		mystack.push(2);
		mystack.push(3);
		mystack.push(0);
		
		System.out.println(mystack.getMin());
		
		mystack.pop();
		
		System.out.println(mystack.getMin());
		
	}

}















