class Solution {
    public long countGoodIntegers(int n, int k) {
        long c=0;
        HashSet<String> h=new HashSet<>();
        if (n%2==0)
        {
            n/=2;
            for(int i=(int)Math.pow(10,n-1);i<Math.pow(10,n);i++)
            {
                String r= new StringBuilder(""+i).reverse().toString();
                r=""+i+r;
                long l1=Long.valueOf(r);
                if(l1%k==0)
                {
                    char[] charArray = r.toCharArray();
                    Arrays.sort(charArray);
                    String sortedString = new String(charArray);
                    h.add(sortedString);
                }
            }
        }
        else
        {
            n-=1;
            n/=2;
            for(int i=(int)Math.pow(10,n);i<Math.pow(10,n+1);i++)
            {
                String r= new StringBuilder((""+i).substring(0,(""+i).length()-1)).reverse().toString();
                r=""+i+r;
                long l1=Long.valueOf(r);
                if(l1%k==0)
                {
                    char[] charArray = r.toCharArray();
                    Arrays.sort(charArray);
                    String sortedString = new String(charArray);
                    h.add(sortedString);
                }
            }
        }
        for(String s1:h)
        {
            long n1=1;
            long d1=1;
            int j=1;
            int j1=0;
            if(s1.charAt(0)=='0')
            {
                j1++;
            }
            for(int i=1;i<s1.length();i++)
            {
                n1*=(i+1);
                if(s1.charAt(i)==s1.charAt(i-1))
                {
                    j++;
                }
                else
                {
                    j=1;
                }
                d1*=j;
                if(s1.charAt(i)=='0')
                {
                    j1++;
                }
            }
            if(j1>0)
            {
                c=c+(n1/d1)-((n1/s1.length())/(d1/j1));
            }
            else
            {
                c=c+(n1/d1);
            }
        }
        return c;
    }
}
