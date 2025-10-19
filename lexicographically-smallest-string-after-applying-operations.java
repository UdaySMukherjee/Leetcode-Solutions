import java.util.*;

class Solution {
    private String rotate(String s, int b) {
        return s.substring(b) + s.substring(0, b); // rotate left by b
    }

    public String findLexSmallestString(String s, int a, int b) {
        Set<String> vis = new HashSet<>();
        Queue<String> q = new LinkedList<>();
        q.add(s);
        String ans = s;

        while (!q.isEmpty()) {
            String temp = q.poll();
            if (vis.contains(temp)) continue;
            vis.add(temp);
            if (temp.compareTo(ans) < 0) ans = temp;

            // Try rotation
            q.add(rotate(temp, b));

            // Try addition
            char[] arr = temp.toCharArray();
            for (int i = 1; i < arr.length; i += 2) {
                arr[i] = (char) (((arr[i] - '0' + a) % 10) + '0');
            }
            q.add(new String(arr));
        }
        return ans;
    }
}
