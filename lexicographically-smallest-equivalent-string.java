class Solution {
    // Inner class to implement the UnionFind data structure
    class UnionFind {
        private int[] parent; // Array to store the parent of each element

        // Constructor: Initializes the UnionFind with 'n' elements
        public UnionFind(int n) {
            parent = new int[n];
            // Initially, each element is its own parent (separate sets)
            for (int i = 0; i < n; i++) {
                parent[i] = i;
            }
        }

        // Find: Finds the root (representative) of the set that 'x' belongs to
        public int find(int x) {
            // If 'x' is its own parent, it's the root
            if (parent[x] == x) {
                return x;
            }
            // Path compression: Update 'x's parent to point directly to the root
            parent[x] = find(parent[x]);
            return parent[x];
        }

        // Union: Merges the sets that 'x' and 'y' belong to
        public void union(int x, int y) {
            int rootX = find(x); // Find the root of 'x'
            int rootY = find(y); // Find the root of 'y'
            // If 'x' and 'y' are in different sets
            if (rootX != rootY) {
                // Attach the larger root to the smaller root to keep the smallest char as representative
                if (rootX < rootY) {
                    parent[rootY] = rootX;
                } else {
                    parent[rootX] = rootY;
                }
            }
        }
    }

    // Main function to find the smallest equivalent string
    public String smallestEquivalentString(String s1, String s2, String baseStr) {
        UnionFind uf = new UnionFind(26); // Create a UnionFind for 26 lowercase letters

        // Build the equivalency map based on s1 and s2
        for (int i = 0; i < s1.length(); i++) {
            char c1 = s1.charAt(i); // Get the character from s1 at index i
            char c2 = s2.charAt(i); // Get the character from s2 at index i
            uf.union(c1 - 'a', c2 - 'a'); // Union the sets of c1 and c2
        }

        // Transform baseStr using the equivalency map
        StringBuilder result = new StringBuilder(); // Use StringBuilder for efficiency
        for (char c : baseStr.toCharArray()) {
            // Find the representative of the set that 'c' belongs to
            // Append the smallest equivalent character to the result
            result.append((char) (uf.find(c - 'a') + 'a'));
        }

        return result.toString(); // Convert StringBuilder to String and return
    }
}
