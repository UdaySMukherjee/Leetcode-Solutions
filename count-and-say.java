class Solution {
    public static String recursivecall(String s, int n){
        if(n==0) return s;

        StringBuilder result  = new StringBuilder();

        int count = 1;
        char curr = s.charAt(0);

        for(int i=1;i<s.length();i++){
            if(curr==s.charAt(i))
                count++;
            else{
                result.append(count);
                result.append(curr);
                count = 1;
                curr =  s.charAt(i);
            }
        }
        result.append(count);
        result.append(curr);

        return recursivecall(result.toString(),n-1);
    }

    public String countAndSay(int n) {
        return recursivecall("1",n-1);
    }
}
