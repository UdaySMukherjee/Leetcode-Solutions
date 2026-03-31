def KMP_search(text, pattern):
    def build_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = build_lps(pattern)
    i = 0  
    j = 0  
    ans = []
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern):
            ans.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return ans




class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        
        basecamp = ['' for i in range(len(str1) + len(str2) - 1)]
        
        movers = []
        mv = set()
        for ea in range(len(str1)):
            if str1[ea] == 'F':
                mv.add(ea)
                
                continue
            for jh in range(len(str2)):
                if jh + ea >= len(basecamp):
                    return ''
                if basecamp[jh + ea] != '' and basecamp[jh + ea] != str2[jh]:
                    print('hit')
                    return ''
                basecamp[jh + ea] = str2[jh]
                
                
        
        
        
        for i in range(len(basecamp)):
            if basecamp[i] == '':
                basecamp[i] = 'a'
                movers.append(i)
                mv.add(i)
                
        text = ''.join(basecamp)
                
        thesis = KMP_search(text, str2)
        
        
        
        for i in range(10000):
            
            hit = False
            for i in thesis:
                if i in mv:
                    latest = i + len(str2) - 1

                    hit = False
                    
                    dunkee = 0
                    
                    idx = bisect.bisect_left(movers, latest - 1)
                    
                    
                    while idx > len(movers):
                        idx -= 1
                    while idx > 0 and movers[idx] > latest:
                        idx -= 1
                    if idx < len(movers) and movers[idx] <= latest:
                        
                        if idx + 1 < len(movers) and movers[idx + 1] <= latest:
                            basecamp[movers[idx + 1]] = 'b'
                            dunkee = movers[idx + 1]
                            hit = True
                            thesis = KMP_search(''.join(basecamp), str2)
                        else:
                            basecamp[movers[idx]] = 'b'
                            dunkee = movers[idx]
                            hit = True
                            
                            anew = [i for i in thesis if i > latest or i < i]
                            
                            thesis = anew
                            # thesis = KMP_search(''.join(basecamp), str2)
                        

                        
                        break;
                    
                    # for ea in movers[::-1]:
                    #     if ea <= latest:
                    #         basecamp[ea] = 'b'
                    #         dunkee = ea
                    #         hit = True
                    #         break
                    if not hit:
                        print('hit', idx, movers, latest)
                        return ''
                    
                    text = ''.join(basecamp)
                    
                  
                        
                    break
                if hit:
                    break
            if not hit:
                
                thesis = KMP_search(''.join(basecamp), str2)
                
                for i in thesis:
                    if i in mv:
                        return ''
                
                return ''.join(basecamp)
                
                        
                        
        
        return ''
        
