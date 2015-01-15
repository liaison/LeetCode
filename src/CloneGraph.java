/**
 * Clone an undirected graph. 
 * Each node in the graph contains a label and a list of its neighbors.
 * 
 * @author Lisong Guo <lisong.guo@me.com>
 * @date   Jan 15, 2015
 *
 */
import java.util.Hashtable;
import java.util.Stack;

public class CloneGraph {

    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
    	if(node == null){
    		return null;
    	}
    	
        Hashtable<Integer, UndirectedGraphNode> nodeTable 
        	= new Hashtable<Integer, UndirectedGraphNode>();
    	
        UndirectedGraphNode newStart = new UndirectedGraphNode(node.label);
        nodeTable.put(newStart.label, newStart);
        
        // Enumerate all nodes to clone 
        Stack<UndirectedGraphNode> toClone = new Stack<UndirectedGraphNode>();
        toClone.push(node);
        
        while(! toClone.isEmpty()){
        	UndirectedGraphNode cur = toClone.pop();
        	UndirectedGraphNode realCur = nodeTable.get(cur.label);
        	
        	// populate the neighbor nodes for the actual current node.
        	for(UndirectedGraphNode n : cur.neighbors){
        		UndirectedGraphNode neighbor = nodeTable.get(n.label);
            	
            	if(neighbor == null){
            		toClone.push(n); // new node to clone
                	
            		neighbor = new UndirectedGraphNode(n.label);
            		nodeTable.put(n.label, neighbor);
            	}
            	
            	realCur.neighbors.add(neighbor);
            }
        }
        
        return newStart;
    }
    
    
	public static void main(String[] args) {
		//{0,1,2#1,2#2,2}.
		UndirectedGraphNode node0 = new UndirectedGraphNode(0);
		UndirectedGraphNode node1 = new UndirectedGraphNode(1);
		UndirectedGraphNode node2 = new UndirectedGraphNode(2);
		
		node0.neighbors.add(node1);
		node0.neighbors.add(node2);
		
		node1.neighbors.add(node2);
		
		node2.neighbors.add(node2);
	}

}
