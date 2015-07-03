/**
 * There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs,
is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0.
So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0,
and to take course 0 you should also have finished course 1. So it is impossible.

 * @author Lisong Guo <lisong.guo@me.com>
 *
 */
import static org.junit.Assert.*;
import org.junit.Test;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Vector;


public class CourseSchedule {

    /**
     * Check if there is a cycle starting from a given node and existing trace.
     */
    private boolean isCyclic(HashMap<Integer, Vector<Integer>> graph,
                             int nodeIndex,
                             HashSet<Integer> parcours) {

        Vector<Integer> neighbours = graph.get(nodeIndex);
        // The bottom case, we reach a node that does not have any outbound links.
        if(neighbours == null){
            return false;
        }

        for(Integer node : neighbours) {
            // If we've seen the node in the trace, then there is a cycle.
            if(parcours.contains(node)) {
                return true;
            }

            // Add this neighbour into the trace, and check starting from
            //  this neighbour if there is a cycle.
            parcours.add(node);
            if(isCyclic(graph, node, parcours)) {
                return true;
            }

            // There is no cycle starting from this neighbour,
            //   remove it from the trace and try another one.
            parcours.remove(node);
        }

        return false;
    }


    public boolean canFinish(int numCourses, int[][] prerequisites) {
        HashMap<Integer, Vector<Integer>> graph =
                new HashMap<Integer, Vector<Integer>>();

        // Construct a linked array to represent the dependency graph of courses.
        for(int [] pair : prerequisites) {
            // pair[1] proceeds (-->) pair[0]
            Vector<Integer> node = graph.get(pair[1]);
            if(node == null) {
                node = new Vector<Integer>();
                graph.put(pair[1], node);
            }
            node.add(pair[0]);
        }

        HashSet<Integer> parcours = new HashSet<Integer>();
        // Iterate all nodes to see if there is any cycle starting from any node.
        for(int nodeIndex = 0; nodeIndex < numCourses; nodeIndex++) {
            parcours.clear();
            if(isCyclic(graph, nodeIndex, parcours)) {
                return false;
            }
        }

        return true;
    }


    @Test
    public void testCanFinish() {
        //int[][] prerequisites = {{1, 0}, {0, 1}};
        int[][] prerequisites = {{1, 0}};

        CourseSchedule cs = new CourseSchedule();
        // exists a cycle in the dependency graph.
        //assertFalse(cs.canFinish(2, prerequisites));

        assertTrue(cs.canFinish(2, prerequisites));

    }

    @Test
    public void testFalseCase() {
        int[][] prerequisites = {{0, 1}, {1, 0}};

        CourseSchedule cs = new CourseSchedule();
        // exists a cycle in the dependency graph.
        assertFalse(cs.canFinish(2, prerequisites));
    }


}











