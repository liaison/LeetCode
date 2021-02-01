import java.util.HashMap;
import java.util.List;

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













