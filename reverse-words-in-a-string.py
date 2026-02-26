class Solution:
    def reverseWords(self, s: str) -> str:
        re=""
        words=s.split()
        for i in range(1,len(words)+1):
            i*=-1
            re+= words[i]+" "
        return re.rstrip()
