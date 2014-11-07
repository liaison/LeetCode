import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

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
		
		
		BinaryTree solution = new BinaryTree();
		
		System.out.println(solution.maxDepth(root));
		
		Utils.printListOfList(solution.levelOrderBottom(root));
		
	}

}










