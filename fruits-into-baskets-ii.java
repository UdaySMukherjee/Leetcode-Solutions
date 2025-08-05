class Solution {
    public int numOfUnplacedFruits(int[] fruits, int[] baskets) {
        ArrayList<Integer> basket = new ArrayList<>();
        for(int i:baskets){
            basket.add(i);
        }
        for(int i=0;i<fruits.length;i++){
            for(int j=0;j<basket.size();j++){
                if(basket.get(j)>=fruits[i]){
                    basket.remove(j);
                    break;
                }
            }
        }
        return basket.size();
    }
}
