public class Solution {

  public void solve(char[][] board) {
    if (board == null || board.length == 0) {
      return;
    }

    HashSet<Integer> Oset = new HashSet<Integer>();
    int rowSize = board.length;
    int columnSize = board[0].length;

    // Identify 'O' and put them into a set
    for (int i = 0; i < board.length; i++) {
      for (int j = 0; j < board[i].length; j++) {
        if (board[i][j] == 'O')
          Oset.add(i * columnSize + j);
      }
    }

    while (true) {
      Iterator<Integer> iter = Oset.iterator();
      if (!iter.hasNext()) {
        break;
      }

      int k = iter.next();
      LinkedList<Integer> bfs = new LinkedList<Integer>();
      bfs.add(k);
      LinkedList<Integer> space = new LinkedList<Integer>();

      boolean isCaptured = true;
      while (!bfs.isEmpty()) {
        // int p = bfs.poll();
        int p = bfs.pollLast();
        Oset.remove(p);
        space.add(p);

        // reach the boundary, therefore no capture.
        if (p % columnSize == 0 || p % columnSize == columnSize - 1 || p / columnSize == 0
            || p / columnSize == rowSize - 1) {
          isCaptured = false;
        }

        // check the neighbors
        int[] offsets = {-1, 1, -columnSize, columnSize};

        for (int offset : offsets) {
          int neighbor = p + offset;
          if (Oset.contains(neighbor))
            bfs.add(neighbor);
          // Oset.remove(neighbor);
        }
      }

      if (isCaptured) {
        // set the space 'O' to 'X'.
        for (Integer p : space) {
          board[p / columnSize][p % columnSize] = 'X';
        }
      }
    }
  }
}
