class Packet {
    int source, destination, timestamp;
    public Packet(int s, int d, int t) {
        source = s;
        destination = d;
        timestamp = t;
    }
}

class Router {
    int memoryLimit;
    Queue<Packet> q;
    HashSet<Long> dupKey;
    HashMap<Integer, ArrayList<Integer>> desToTime;

    // Constructor
    public Router(int memoryLimit) {
        this.memoryLimit = memoryLimit;
        q = new LinkedList<>();
        dupKey = new HashSet<>();
        desToTime = new HashMap<>();
    }

    // Encode packet to a unique long
    private long makeKey(int s, int d, int t) {
        return (long)s * 10000000000L + (long)d * 100000 + t;
    }

    // Add packet
    public boolean addPacket(int source, int destination, int timestamp) {
        long key = makeKey(source, destination, timestamp);
        if (dupKey.contains(key)) return false;

        // Evict oldest if memory full
        if (q.size() == memoryLimit) {
            Packet old = q.poll();
            long oldKey = makeKey(old.source, old.destination, old.timestamp);
            dupKey.remove(oldKey);

            ArrayList<Integer> list = desToTime.get(old.destination);
            list.remove(0); // remove oldest timestamp
            if (list.isEmpty()) desToTime.remove(old.destination);
        }

        Packet p = new Packet(source, destination, timestamp);
        q.add(p);
        dupKey.add(key);
        desToTime.putIfAbsent(destination, new ArrayList<>());
        desToTime.get(destination).add(timestamp);
        return true;
    }

    // Forward packet
    public int[] forwardPacket() {
        if (q.isEmpty()) return new int[0];
        Packet p = q.poll();

        long key = makeKey(p.source, p.destination, p.timestamp);
        dupKey.remove(key);

        ArrayList<Integer> list = desToTime.get(p.destination);
        list.remove(0);
        if (list.isEmpty()) desToTime.remove(p.destination);

        return new int[]{p.source, p.destination, p.timestamp};
    }

    // Count packets by destination and timestamp range
    public int getCount(int destination, int startTime, int endTime) {
        if (!desToTime.containsKey(destination)) return 0;
        ArrayList<Integer> list = desToTime.get(destination);
        // Binary search since timestamps are increasing
        int left = lowerBound(list, startTime);
        int right = upperBound(list, endTime);
        return right - left;
    }

    // Helper: lower_bound
    private int lowerBound(ArrayList<Integer> list, int target) {
        int l = 0, r = list.size();
        while (l < r) {
            int m = (l + r) / 2;
            if (list.get(m) >= target) r = m;
            else l = m + 1;
        }
        return l;
    }

    // Helper: upper_bound
    private int upperBound(ArrayList<Integer> list, int target) {
        int l = 0, r = list.size();
        while (l < r) {
            int m = (l + r) / 2;
            if (list.get(m) > target) r = m;
            else l = m + 1;
        }
        return l;
    }
}

/**
 * Your Router object will be instantiated and called as such:
 * Router obj = new Router(memoryLimit);
 * boolean param_1 = obj.addPacket(source,destination,timestamp);
 * int[] param_2 = obj.forwardPacket();
 * int param_3 = obj.getCount(destination,startTime,endTime);
 */
