import java.util.Stack;

/**
 * Implement an iterator over a binary search tree (BST). 
 * Your iterator will be initialized with the root node of a BST.
 
   Calling next() will return the next smallest number in the BST.

   Note: next() and hasNext() should run in average O(1) time and
    uses O(h) memory, where h is the height of the tree.

 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Jan 1, 2015
 *
 */
public class BSTIterator {

    //! keep the next h element at most in the memory.
    // in order to achieve O(1) retrieval time with only O(h) cost.
    Stack<TreeNode> stack = new Stack<TreeNode>();

    private void refreshStack(TreeNode iter){
         while(iter != null){
             stack.push(iter);
             iter = iter.left;
         }
    }

    public BSTIterator(TreeNode root) {
       this.refreshStack(root);
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !(stack.isEmpty());
    }

    /** @return the next smallest number */
    public int next() {
        TreeNode node = stack.pop();
        if(node != null){
            this.refreshStack(node.right);
            return node.val;
        }
 
        return -1; // should throw exception here.
    }


    public static void main(String[] args) {
        TreeNode root = new TreeNode(2);
        TreeNode left = new TreeNode(1);
        TreeNode right = new TreeNode(3);

        root.left = left;
        root.right = right;
		
        BSTIterator iter = new BSTIterator(root);
		
        while(iter.hasNext()){
            System.out.println(iter.next());
        }
    }

}
