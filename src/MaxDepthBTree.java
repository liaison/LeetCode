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
	 *  Desired solution function
	 * @return
	 */
	public int maxDepth(TreeNode root) {
		if(root == null){
			return 0;
		}
		
		int leftTreeDepth = 0;		
		if(root.left != null){
			leftTreeDepth = maxDepth(root.left);
		}
		
		int rightTreeDepth = 0;
		if(root.right != null){
			rightTreeDepth = maxDepth(root.right);
		}
			
		return Math.max(leftTreeDepth, rightTreeDepth) + 1;
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










