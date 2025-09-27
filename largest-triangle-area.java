class Solution {
    public double largestTriangleArea(int[][] points) {
        double maxArea = 0;
        int n = points.length;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = j + 1; k < n; k++) {
                    // Calculate side lengths of the triangle
                    double a = getDist(points[i], points[j]);
                    double b = getDist(points[j], points[k]);
                    double c = getDist(points[k], points[i]);

                    // Semi-perimeter
                    double S = (a + b + c) / 2.0;

                    // Heron's formula: Area^2 = S(S-a)(S-b)(S-c)
                    double radicand = S * (S - a) * (S - b) * (S - c);

                    // Numerical safeguard: avoid negative due to floating-point precision
                    radicand = Math.max(0.0, radicand);

                    double area = Math.sqrt(radicand);

                    // Track the maximum area
                    maxArea = Math.max(maxArea, area);
                }
            }
        }
        return maxArea;
    }

    // Helper method to compute Euclidean distance between two points
    private double getDist(int[] p1, int[] p2) {
        int dx = p1[0] - p2[0];
        int dy = p1[1] - p2[1];
        return Math.sqrt(dx * dx + dy * dy);
    }
}
