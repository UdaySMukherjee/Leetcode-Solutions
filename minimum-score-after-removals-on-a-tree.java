class Solution {
    private int[] subtreeXor;
    private Set<Integer>[] descendants;
    private List<Integer>[] tree;

    private void dfs(int node, int parent, int[] nums) {
        subtreeXor[node] = nums[node];
        descendants[node].add(node);

        for (int neighbor : tree[node]) {
            if (neighbor != parent) {
                dfs(neighbor, node, nums);
                subtreeXor[node] ^= subtreeXor[neighbor];
                descendants[node].addAll(descendants[neighbor]);
            }
        }
    }

    public int minimumScore(int[] nums, int[][] edges) {
        int n = nums.length;
        
        // Initialize tree structure
        tree = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            tree[i] = new ArrayList<>();
        }
        for (int[] edge : edges) {
            tree[edge[0]].add(edge[1]);
            tree[edge[1]].add(edge[0]);
        }

        // Initialize DFS data structures
        subtreeXor = new int[n];
        descendants = new HashSet[n];
        for (int i = 0; i < n; i++) {
            descendants[i] = new HashSet<>();
        }
        
        // Perform DFS to compute subtree XORs and descendants
        dfs(0, -1, nums);
        
        int totalXor = subtreeXor[0];
        int minScore = Integer.MAX_VALUE;

        // Evaluate all possible node pairs
        for (int i = 1; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                int xorI = subtreeXor[i];
                int xorJ = subtreeXor[j];
                int val1, val2, val3;

                if (descendants[i].contains(j)) {
                    // j is in i's subtree
                    val1 = xorJ;
                    val2 = xorI ^ xorJ;
                    val3 = totalXor ^ xorI;
                } else if (descendants[j].contains(i)) {
                    // i is in j's subtree
                    val1 = xorI;
                    val2 = xorJ ^ xorI;
                    val3 = totalXor ^ xorJ;
                } else {
                    // Independent subtrees
                    val1 = xorI;
                    val2 = xorJ;
                    val3 = totalXor ^ xorI ^ xorJ;
                }
                
                // Calculate current score
                int currentScore = Math.max(val1, Math.max(val2, val3)) - 
                                  Math.min(val1, Math.min(val2, val3));
                minScore = Math.min(minScore, currentScore);
            }
        }

        return minScore;
    }
}
