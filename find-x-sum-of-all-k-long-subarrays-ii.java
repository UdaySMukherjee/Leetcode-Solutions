import java.util.*;

class Solution {

    // Represents a number and its frequency
    static class Element implements Comparable<Element> {
        int num, freq;
        Element(int num, int freq) { this.num = num; this.freq = freq; }

        // Order by frequency ascending, then number ascending
        public int compareTo(Element o) {
            if (this.freq != o.freq) return this.freq - o.freq;
            return this.num - o.num;
        }

        // Equality based on both num and freq
        @Override
        public boolean equals(Object obj) {
            if (!(obj instanceof Element)) return false;
            Element o = (Element)obj;
            return this.num == o.num && this.freq == o.freq;
        }

        @Override
        public int hashCode() {
            return Objects.hash(num, freq);
        }
    }

    long sum = 0; // Sum of freq * num for elements in topXSet
    int X; // Many methods need to use, so make it global
    HashMap<Integer, Integer> freqMap = new HashMap<>();
    TreeSet<Element> topXSet = new TreeSet<>();  // Top X elements
    TreeSet<Element> otherSet = new TreeSet<>(); // All other elements

    public long[] findXSum(int[] nums, int k, int x) {
        X = x;
        long[] res = new long[nums.length - k + 1];

        // Initialize frequency map
        for (int num : nums) freqMap.put(num, 0);

        int l = 0;
        for (int r = 0; r < nums.length; r++) {
            update(nums[r], 1); // Add right element to window

            // Shrink window if size exceeds k
            if (r - l + 1 > k) {
                update(nums[l], -1); // Remove leftmost
                l++;
            }

            // Record sum when window size == k
            if (r - l + 1 == k) {
                res[l] = sum;
            }
        }

        return res;
    }

    // Update frequency and adjust sets accordingly
    private void update(int num, int delta) {
        int oldFreq = freqMap.get(num);
        int newFreq = oldFreq + delta;
        freqMap.put(num, newFreq);

        Element oldElem = new Element(num, oldFreq);
        Element newElem = new Element(num, newFreq);

        // Remove the old frequency state
        remove(oldElem);
        // Add the new frequency state
        add(newElem);
    }

    // Add element into correct set
    private void add(Element elem) {
        if (elem.freq == 0) return;

        // If top set not full, add directly
        if (topXSet.size() < X) {
            topXSet.add(elem);
            sum += (long) elem.freq * elem.num;
            return;
        }

        Element smallestTop = topXSet.first();
        // If element belongs in top X
        if (elem.compareTo(smallestTop) > 0) {
            topXSet.pollFirst();
            sum -= (long) smallestTop.freq * smallestTop.num;
            otherSet.add(smallestTop);

            topXSet.add(elem);
            sum += (long) elem.freq * elem.num;
        } else {
            otherSet.add(elem);
        }
    }

    // Remove element from correct set and rebalance
    private void remove(Element elem) {
        if (elem.freq == 0) return;

        // Try remove from otherSet
        if (otherSet.remove(elem)) return;

        // If in topXSet, remove and rebalance from otherSet
        if (topXSet.remove(elem)) {
            sum -= (long) elem.freq * elem.num;
            if (!otherSet.isEmpty()) {
                Element maxBot = otherSet.pollLast();
                topXSet.add(maxBot);
                sum += (long) maxBot.freq * maxBot.num;
            }
        }
    }
}
