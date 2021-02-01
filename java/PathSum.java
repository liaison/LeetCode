/**
 * 
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Mars 08, 2015
 *
 */
import java.util.List;
import java.util.LinkedList;

public class PathSum {


	/**
	 * Given a binary tree and a sum, 
	 * find all root-to-leaf paths where each path's sum equals the given sum.

	For example:
		Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
	return
	[
   		[5,4,11,2],
   		[5,8,4,5]
	]
	 */
	List<List<Integer>> res = new LinkedList<List<Integer>>();
    
	private void pathSum_rec(LinkedList<Integer> path, TreeNode cur, int sum) {
		
		// push this node into the path.
		path.add(cur.val);
		sum -= cur.val;
		
		// First, check the left sub-tree.
		if (cur.left != null) {
			pathSum_rec(path, cur.left, sum);
		} 
		
		// then, check the right sub-tree.
		if (cur.right != null) {
			pathSum_rec(path, cur.right, sum);
		} 
		
		// Reach leave, check if the sum is also reached.	
		if (cur.left ==  null && cur.right == null && sum == 0) {
			List<Integer> newPath = new LinkedList<Integer>();
			newPath.addAll(path);
			res.add(newPath);
		}
		
		// pop out this node out of the path
		path.removeLast();
	}
	
	public List<List<Integer>> pathSum(TreeNode root, int sum) {
		LinkedList<Integer> path = new LinkedList<Integer>();
		
		if (root != null) {
			pathSum_rec(path, root, sum);	
		}
		
		return res;
    }
    
	
	public static void main(String[] args) {
		
		/*
		BinaryTree bt = new BinaryTree();
		int [] preorder = {5, 4, 11, 7, 2, 8, 13, 4, 5, 1};
		int [] inorder = {7, 11, 2, 4, 5, 13, 8, 5, 4, 1};
		TreeNode root = bt.buildTree(preorder, inorder);
		int sum = 22;
		*/
		
		TreeNode root = new TreeNode(10);
		TreeNode left = new TreeNode(12);
		TreeNode right = new TreeNode(13);
		root.left = left;
		root.right = right;
		int sum = 22;
		
		
		/*
		TreeNode root = new TreeNode(1);
		TreeNode left = new TreeNode(2);
		root.left = left;
		int sum = 1;
		*/
		
		PathSum ps = new PathSum();
		Utils.printListOfList(ps.pathSum(root, sum));
	}

}








