

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















