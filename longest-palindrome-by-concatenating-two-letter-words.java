class Solution {
    public int longestPalindrome(String[] words) {
        // use as a map to store frequency of each element
        int[] freq = new int[1024];
        for(String word : words){
            //encode an element into integer key
            int key =(word.charAt(0)-'a');
            key = (key<<5) | (word.charAt(1)-'a');            
            freq[key]++;
        }
        int length = 0; // length of palindrone string
        boolean isOddSymmetric = false; // if there is a central element for odd length string 

        for(int key =0; key < 1024; key++){
            if(freq[key]==0)continue;

            // generate the reverse key eg (ef for fe)
            int reflection = (key&31)<<5;
            reflection = reflection | ((key&992)>>5);

            int min; // minimum pair that could be formed
            if(key != reflection)min = Math.min(freq[key], freq[reflection]);
            else {
                min = freq[key]/2;
                if((freq[key]&1)==1)isOddSymmetric=true;
            }
            
            length += min*2*2; // each pair will have 4 chars
            freq[key]-=min; freq[reflection]-=min; //remove used pairs
        }

        if(isOddSymmetric)length+=2;

        return length;
    }
}
