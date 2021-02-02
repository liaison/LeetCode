import java.util.HashMap;
import java.util.List;
import java.util.PriorityQueue;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;


class NetworkDelayTime_743 {

    public int networkDelayTime(int[][] times, int n, int k) {

        HashMap<Integer, List<Pair<Integer, Integer>>> graph = new HashMap<>();

        for (int [] entry : times) {
            Integer source = entry[0], target = entry[1], weight = entry[2];
            if (! graph.containsKey(source))
                graph.put(source, new ArrayList<Pair<Integer,Integer>>());
            Pair<Integer, Integer> newEdge = new Pair<>(weight, target);
            graph.get(source).add(newEdge);
        }

        // Sort the outgoing edges based on the weight
        for (List<Pair<Integer, Integer>> edges : graph.values()) {
            Collections.sort(edges, Comparator.comparing(p -> p.getKey()));
        }

        HashMap<Integer, Integer> dist = new HashMap<>();
        dfs(k, 0, graph, dist);

        return dist.size() == n ? Collections.max(dist.values()) : -1;
    }

    /**
     *  Run a DFS traversal, with a global "elapsed" time in a Greedy strategy.
     * @param curr
     * @param elapse
     * @param graph
     * @param dist
     */
    private void dfs(Integer curr, Integer elapse,
                     HashMap<Integer, List<Pair<Integer, Integer>>> graph,
                     HashMap<Integer, Integer> dist) {

        if (dist.containsKey(curr)) {
            if (elapse >= dist.get(curr))
                return;
        }

        dist.put(curr, elapse);

        if (! graph.containsKey(curr))
            return;

        for (Pair<Integer, Integer> entry : graph.get(curr)) {
            Integer weight = entry.getKey();
            Integer target = entry.getValue();
            dfs(target, elapse + weight, graph, dist);
        }
    }
}




class SolutionDijkstra {
    public int networkDelayTime(int[][] times, int n, int k) {

        HashMap<Integer, List<Pair<Integer, Integer>>> graph = new HashMap<>();

        for (int [] entry : times) {
            Integer source = entry[0], target = entry[1], weight = entry[2];
            if (! graph.containsKey(source))
                graph.put(source, new ArrayList<Pair<Integer,Integer>>());
            Pair<Integer, Integer> newEdge = new Pair<>(weight, target);
            graph.get(source).add(newEdge);
        }

        PriorityQueue<Integer[]> queue = new PriorityQueue<>(
            n, Comparator.comparing(p -> p[0]));

        List<Pair<Integer, Integer>> emptyEdgeList = new ArrayList<>();

        // init the PriorityQueue with the neighbors of the starting point
        for (Pair<Integer, Integer> entry : graph.getOrDefault(k, emptyEdgeList)) {
            queue.add(new Integer[]{entry.getKey(), entry.getValue()});
        }

        // target: distance_to_target
        HashMap<Integer, Integer> dist = new HashMap<>();
        dist.put(k, 0);

        while (queue.size() > 0) {
            Integer[] entry = queue.poll();

            Integer timestamp = entry[0], curr = entry[1];

            if (dist.containsKey(curr))
                continue;

            dist.put(curr, timestamp);

            for (Pair<Integer, Integer> neighbor : graph.getOrDefault(curr, emptyEdgeList)) {
                Integer weight = neighbor.getKey(), target = neighbor.getValue();
                if (! dist.containsKey(target))
                    queue.add(new Integer[]{timestamp + weight, target});
            }
        }

        return dist.size() == n ? Collections.max(dist.values()) : -1;
    }
}













