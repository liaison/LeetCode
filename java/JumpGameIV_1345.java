import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.List;

class JumpGameIV_1345 {

    public int minJumps(int[] arr) {

        HashMap<Integer, List<Integer>> valueMap = new HashMap<>();

        // Build the {value: [index]} map
        for (int index = 0; index < arr.length; ++ index ) {
            Integer value = arr[index];
            valueMap.putIfAbsent(value, new ArrayList<Integer>());
            valueMap.get(value).add(index);
        }

        LinkedList<Integer> queue = new LinkedList<Integer>();
        queue.offer(0);
        boolean [] visited = new boolean[arr.length];
        int steps = 0;

        // Running the BFS traversal
        while (queue.size() > 0) {
            LinkedList<Integer> nextQueue = new LinkedList<Integer>();

            // construct the list of nodes to visit in the next level/round
            while (queue.size() > 0) {
                Integer curr = queue.pollFirst();
                Integer value = arr[curr];
                visited[curr] = true;

                if (curr == arr.length - 1)
                    return steps;

                // check the neighbors with the same value
                for (Integer neighbor : valueMap.get(value)) {
                    if (! visited[neighbor])
                        nextQueue.offer(neighbor);
                }
                valueMap.get(value).clear();

                // check the neighbors at adjacent index
                for (int neighbor : new int[]{curr -1, curr + 1}) {
                    if (neighbor < 0 || neighbor == arr.length)
                        continue;
                    if (! visited[neighbor])
                        nextQueue.offer(neighbor);
                }
            }

            queue = nextQueue;
            steps += 1;
        }

        return steps;
    }


    public int minJumps_BidirectionalBFS(int[] arr) {

        HashMap<Integer, List<Integer>> valueMap = new HashMap<>();

        // Build the {value: [index]} map
        for (int index = 0; index < arr.length; ++ index ) {
            Integer value = arr[index];
            valueMap.putIfAbsent(value, new ArrayList<Integer>());
            valueMap.get(value).add(index);
        }

        HashSet<Integer> headQueue = new HashSet<Integer>();
        HashSet<Integer> tailQueue = new HashSet<Integer>();

        headQueue.add(0);
        tailQueue.add(arr.length-1);

        boolean [] visited = new boolean[arr.length];
        int steps = 0;

        // Running the bidirectional BFS traversal,
        //   always starts from the headQueue
        while (headQueue.size() > 0) {

            // pick the level/queue with fewer number of elements to explore
            if (headQueue.size() > tailQueue.size()) {
                HashSet<Integer> temp = headQueue;
                headQueue = tailQueue;
                tailQueue = temp;
            }

            HashSet<Integer> nextQueue = new HashSet<Integer>();
            // construct the list of nodes to visit in the next level/round
            for (Integer curr : headQueue) {
                Integer value = arr[curr];
                visited[curr] = true;

                // when the two queues meet in the middle, the traversal is done.
                if (tailQueue.contains(curr))
                    return steps;

                // check the neighbors with the same value
                for (Integer neighbor : valueMap.get(value)) {
                    if (! visited[neighbor])
                        nextQueue.add(neighbor);
                }
                valueMap.get(value).clear();

                // check the neighbors at adjacent index
                for (int neighbor : new int[]{curr -1, curr + 1}) {
                    if (neighbor < 0 || neighbor == arr.length)
                        continue;
                    if (! visited[neighbor])
                        nextQueue.add(neighbor);
                }
            }

            headQueue = nextQueue;
            steps += 1;
        }

        return steps;
    }

}















