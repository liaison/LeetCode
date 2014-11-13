import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Stack;

/**
 * Given a binary tree, find its maximum depth.
 *
 * The maximum depth is the number of nodes along the longest path from 
 *   the root node down to the farthest leaf node.
 * 
 * @author Lisong Guo <lisong.guo@inria.fr>
 * @date   Nov 06, 2014
 */

public class BinaryTree {

	/**
	 *  Desired solution function. A recursive solution.
	 * @return
	 
	public int maxDepth(TreeNode root) {
		if(root == null){
			return 0;
		}
			
		return Math.max(maxDepth(root.left), maxDepth(root.right)) + 1;
	}
	*/
			
	/**
	 *  A non-recursive solution, with Breadth First Search BFS through a queue.
	 *  
	 *  One can peek, push and pop the element on the head and tail of a LinkedList in java.
	 * @param root
	 * @return
	 */
	public int maxDepth(TreeNode root){
		if(root == null){
			return 0;
		}
		
		LinkedList<TreeNode> queue = new LinkedList<TreeNode>();
		int depth = 0;
		
		queue.add(root);
		TreeNode lastLevel = root;
		
		while(! queue.isEmpty()){
			TreeNode curr = queue.poll();
			if(curr.left != null) queue.offer(curr.left);
			if(curr.right != null) queue.offer(curr.right);
			
			if(curr == lastLevel){
				lastLevel = queue.peekLast();
				depth ++;
			}
		}
		
		return depth;
	}
	
	/**
	 * 
	 * Given a binary tree, return the bottom-up level order traversal of its nodes' values.
	 *  (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
	 */
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        
    	List<List<Integer>> result = new ArrayList<List<Integer>>();
        
        if(root == null){
        	return result;
        }
    	
        TreeNode lastLevel = root;
        LinkedList<TreeNode> queue = new LinkedList<TreeNode>();
        queue.offer(root);
                
        ArrayList<Integer> levelArray = new ArrayList<Integer>();
        while(! queue.isEmpty()){
        	
        	TreeNode curr = queue.poll();
        	levelArray.add(curr.val);
        	
        	if(curr.left != null) queue.offer(curr.left);
        	if(curr.right != null) queue.offer(curr.right);
        	
        	if(curr == lastLevel){
        		lastLevel = queue.peekLast();
        		result.add(0, levelArray);
        		levelArray = new ArrayList<Integer>();
        	}
        }
        
        return result;
    }
    
    
    /**
     * 
     * Given a binary tree, check whether it is a mirror of itself 
     		(ie, symmetric around its center).

	    For example, this binary tree is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
     * 		This is a recursive solution.
     */
    public boolean isSymmetric(TreeNode root) {
    	// empty tree is considered to be symmetric 
    	if(root == null){
    		return true;
    	}
    	
    	return isSymmetric_rec(root.left, root.right);
    }
    
    
    private boolean isSymmetric_rec(TreeNode t1, TreeNode t2){
    	if(t1 != t2 ){
    		if( t1 != null && t2 != null){
    			if(t1.val != t2.val){
    				return false;
    			}
    			return isSymmetric_rec(t1.left, t2.right) && 
    				   isSymmetric_rec(t1.right, t2.left);
    		}else if(t1 == null && t2 == null){
    			return true;
    		}else{
    			return false;
    		}
    	}else{
    		return true;
    	}
    }
    
    
    /**
     * Compare nodes two by two, in an iterative way.
     */
    public boolean isSymmetric_iter(TreeNode root){
    	if(root == null){
    		return true;
    	}
    	
    	LinkedList<TreeNode> queue = new LinkedList<TreeNode>();
    	queue.offer(root.left);
    	queue.offer(root.right);
    	while(! queue.isEmpty()){
    		TreeNode left = queue.poll();
    		TreeNode right = queue.poll();
    		
    		if(left != null && right != null){
    			if(left.val != right.val){
    				return false;
    			}else{
    				queue.offer(left.left);
    				queue.offer(right.right);
    				queue.offer(left.right);
    				queue.offer(right.left);
    			}
    		}else if(left != null || right != null){
    			return false;
    		}
    	}
    	return true;
    }
    
    
    /**
     * Given a binary tree, return the preorder traversal of its nodes' values.
     * 
     * Note: Recursive solution is trivial, could you do it iteratively?
     * 
     */
    public List<Integer> preorderTraversal(TreeNode root) {
    	
    	Stack<TreeNode> stack = new Stack<TreeNode>();
    	LinkedList<Integer> res = new LinkedList<Integer>();
    	
    	if(root == null){
    		return res;
    	}else{
        	stack.push(root);
    	}
    	
    	while(! stack.isEmpty()){
    		TreeNode head = stack.pop();
    		res.add(head.val);
    		
    		if(head.right != null){
    			stack.push(head.right);
    		}
    		
    		if(head.left != null){
    			stack.push(head.left);
    		}
    	}
    	
    	return res;
    }
    
    
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		
		TreeNode root = new TreeNode(1);
		TreeNode left = new TreeNode(2);
		TreeNode right = new TreeNode(2);
		root.left = left;
		root.right = right;
		
		left.left = new TreeNode(4);
		right.right = new TreeNode(4);
		
		//left.right.right = new TreeNode(6);
		
		BinaryTree solution = new BinaryTree();
		
		System.out.println(solution.maxDepth(root));
		
		Utils.printListOfList(solution.levelOrderBottom(root));
		
		
		// input {1, 2}, expected result false
		TreeNode a = new TreeNode(1);
		a.left = new TreeNode(2);
		
		System.out.println(solution.isSymmetric_iter(root));
		
		
		Utils.printList(solution.preorderTraversal(root));
		
	}

}










