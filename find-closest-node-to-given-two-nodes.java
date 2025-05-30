class Solution {
    static final int MARK1 = 1;
    static final int MARK2 = 2;
    static final int MARK_BOTH = MARK1 | MARK2;

    public int closestMeetingNode(int[] edges, int node1, int node2) {
        int totalNodes = edges.length;
        byte[] state = new byte[totalNodes];
        int meetingNode = Integer.MAX_VALUE;

        while (meetingNode == Integer.MAX_VALUE && node1 >= 0 && node2 >= 0) {
            if ((state[node1] & MARK1) != 0)
                node1 = -1;
            else if ((state[node1] |= MARK1) == MARK_BOTH)
                meetingNode = node1;
            else
                node1 = edges[node1];

            if ((state[node2] & MARK2) != 0) {
                node2 = -1;
                break;
            }
            if ((state[node2] |= MARK2) == MARK_BOTH) {
                meetingNode = Math.min(meetingNode, node2);
                break;
            }
            node2 = edges[node2];
        }

        if (meetingNode != Integer.MAX_VALUE) return meetingNode;

        if (node1 >= 0) {
            while (node1 >= 0) {
                if ((state[node1] & MARK1) != 0) return -1;
                if ((state[node1] |= MARK1) == MARK_BOTH) return node1;
                node1 = edges[node1];
            }
            return -1;
        }

        while (node2 >= 0) {
            if ((state[node2] & MARK2) != 0) return -1;
            if ((state[node2] |= MARK2) == MARK_BOTH) return node2;
            node2 = edges[node2];
        }

        return -1;
    }
}
