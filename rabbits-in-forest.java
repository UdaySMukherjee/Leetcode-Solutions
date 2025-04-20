class Solution {
    public int numRabbits(int[] answers) {
        Arrays.sort(answers);
        int temp=0;
        int count=0;
        for(int i=0;i<answers.length;i++){
            if(answers[i]==0){
                count++;
            }
            else if(i>0 && answers[i] != answers[i-1] || temp == 0){
                count+= answers[i]+1;
                temp = answers[i];
            }
            else{
                temp --;
            }
        }
        return count;
    }
}
