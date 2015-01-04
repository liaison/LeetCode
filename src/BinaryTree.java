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
        
    	List<List<Integer>> result = new LinkedList<List<Integer>>();
        
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
     * Given two binary trees, write a function to check if they are equal or not.
		Two binary trees are considered equal if they are structurally identical and 
		the nodes have the same value.
     */
    public boolean isSameTree(TreeNode p, TreeNode q) {
    	if(p == null && q == null){
    		return true;
    	
    	}else if(p == null && q != null  ||
    			 p != null && q == null){
    		return false;
    	}else{
    		// neither p nor q is NULL, check both left and right subtree
        	
    		if(p.val != q.val){
    			return false;
    		}
        	return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    	}	
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
     * Given a singly linked list where elements are sorted in ascending order, 
     * 		convert it to a height balanced BST
     * @return
    
    public TreeNode sortedListToBST(ListNode head) {
        int size = 0;
        while(head )
    }
     */
    
    /**
	Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that 
		adding up all the values along the path equals the given sum.

	For example:
	Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1

	return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
    
     */

	public boolean hasPathSum(TreeNode root, int sum) {

		if (root == null) {
			return false;
		}

		sum = sum - root.val;

		if (root.left == null && root.right == null) {
			if (sum == 0) {
				return true;
			}
		}
		
		// To see if there is a path in the left subtree 
		//		that satisfy the constraint.
		if (root.left != null) {
			if (hasPathSum(root.left, sum)) {
				return true;
			}
		}

		// Try the right tree.
		if (root.right != null) {
			if (hasPathSum(root.right, sum)) {
				return true;
			}
		}
		
		// both left and right substree do not satisfy the constraint.
		return false;
	}
    
    /**
     * 
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

     * @param root
     * @return
     */
    public List<Integer> postorderTraversal(TreeNode root) {
    	Stack<TreeNode> traversal = new Stack<TreeNode>();
    	List<Integer> res = new LinkedList<Integer>();
    	
    	if(root == null)
    		return res;
    	
    	traversal.push(root);
    	while(!traversal.isEmpty()){
    		TreeNode top = traversal.pop();
    		res.add(0, top.val);
    		
    		if(top.left != null){
    			traversal.push(top.left);
    		}
    		
    		if(top.right != null){
    			traversal.push(top.right);
    		}
    	}
    	return res;
    }
   
   
    public List<Integer> inorderTraversal(TreeNode root) {
    	Stack<TreeNode> stack = new Stack<TreeNode>();
    	List<Integer> res = new LinkedList<Integer>();
    	
    	if(root == null)
    		return res;
    	    	
    	stack.push(root);
    	
    	while(!stack.isEmpty()){
    		TreeNode top = stack.pop();

    		res.add(0, top.val);
    	    		
    		if(top.left != null){
    			stack.push(top.left);
    		}
	
    		if(top.right != null){
    			stack.push(top.right);
    		}
    	}
    	return res;
        
    }
    
    
    private class BalanceResult {
    	boolean isBalanced; 
    	int size;
    	
    	BalanceResult(boolean b, int s){
    		isBalanced = b;
    		size = s;
    	}
    }
    
    private BalanceResult isBalanced_rec(TreeNode root){
    	if(root == null){
    		return new BalanceResult(true, 0);
    	}
    	
    	BalanceResult left = isBalanced_rec(root.left);
    	BalanceResult right = isBalanced_rec(root.right);
    
    	if(!left.isBalanced || !right.isBalanced){
    		return new BalanceResult(false, -1);
    	}else{
    		if(Math.abs(left.size - right.size) > 1){
    			return new BalanceResult(false, -1);
    		}else{
    			int newSize = Math.max(left.size, right.size)+1;
    			return new BalanceResult(true, newSize);
    		}
    	}
    }
    
    /**
     * 
     * Given a binary tree, determine if it is height-balanced.
		For this problem, a height-balanced binary tree is defined as a binary tree 
		in which the depth of the two subtrees of every node never differ by more than 1.
     */
    public boolean isBalanced(TreeNode root) {
    	return isBalanced_rec(root).isBalanced;
    }
    
    
    public int minDepth(TreeNode root) {
    	if(root == null){
    		return 0;
    	}
    	
    	if(root.left == null && root.right == null){
    		return 1;
    	}
    	
    	if(root.left == null){
    		return minDepth(root.right)+1;
    	}else if(root.right == null){
    		return minDepth(root.left)+1;
    	}else{
    		return Math.min(minDepth(root.left), minDepth(root.right))+1;
    	}
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
		
		System.out.println(solution.isBalanced(root));
		
		System.out.println(solution.maxDepth(root));
		
		System.out.println(solution.minDepth(root));
		
		Utils.printListOfList(solution.levelOrderBottom(root));
		
		
		// input {1, 2}, expected result false
		TreeNode a = new TreeNode(1);
		a.left = new TreeNode(2);
		
		System.out.println(solution.isSymmetric_iter(root));
		
		
		Utils.printList(solution.preorderTraversal(root));
		
		
		TreeNode postOrderRoot = new TreeNode(1);
		TreeNode postOrderRight = new TreeNode(2);
		TreeNode postOrderLeft = new TreeNode(3);
		postOrderRoot.right = postOrderRight;
		postOrderRight.left = postOrderLeft;
		
		Utils.printList(solution.postorderTraversal(postOrderRoot));
		
		System.out.println(solution.hasPathSum(a, 3));
		
		System.out.println(solution.minDepth(postOrderRoot));
	}

}










