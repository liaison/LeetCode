import java.util.ArrayList;
import java.util.LinkedList;

/**
 * Given a binary tree, find its maximum depth.
 *
 * The maximum depth is the number of nodes along the longest path from 
 *   the root node down to the farthest leaf node.
 * 
 * @author Lisong Guo <lisong.guo@inria.fr>
 * @date   Nov 06, 2014
 */

public class MaxDepthBTree {

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
	 *  A non-recursive solution, with Width First Search WFS through a queue.
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
	 * @param args
	 */
	public static void main(String[] args) {
		
		TreeNode root = new TreeNode(1);
		TreeNode left = new TreeNode(2);
		TreeNode right = new TreeNode(3);
		root.left = left;
		root.right = right;
		
		left.left = new TreeNode(4);
		left.right = new TreeNode(5);
		
		left.right.right = new TreeNode(6);
		
		
		MaxDepthBTree solution = new MaxDepthBTree();
		
		System.out.println(solution.maxDepth(root));
		
	}


}










