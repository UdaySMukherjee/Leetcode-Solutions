class Solution {
    public int totalFruit(int[] fruits) {
        int start = 0,end = 0;
        int n = fruits.length;
        int maxlength = 0;
        Map<Integer,Integer> mp = new HashMap<>();
        while(end<n)
        {
            mp.put(fruits[end],mp.getOrDefault(fruits[end],0)+1);
            while(mp.size()>=3)
            {
                mp.put(fruits[start],mp.get(fruits[start])-1);
                if(mp.get(fruits[start]) == 0)
                mp.remove(fruits[start]);
                start++;
            }
            int currlength = end-start+1;
            maxlength = Math.max(maxlength,currlength);
            end++;
        }
        return maxlength;
    }
}
