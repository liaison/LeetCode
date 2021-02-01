class Solution {
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
}










