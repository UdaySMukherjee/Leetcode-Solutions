class Solution:
# use 2-pointer
    def compressedString(self, word: str) -> str:
        n, l, r= len(word), 0, 0
        ans=[]
        while r<n:
            c=word[l]
            while r<n and word[r]==c:
                r+=1
            q, rem=divmod(r-l, 9)
            for _ in range(q):# ans+=('9'+c)*q
                ans+='9'+c    # can replace by this
            if rem>0:
                ans+=str(rem)+c
            l=r
        return "".join(ans)
        
        
