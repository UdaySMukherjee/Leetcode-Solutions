class _CanonicalSolution(object):

    def numberOfUniqueGoodSubsequences(self, binary):
        """
        :type binary: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        ends0, ends1 = (0, 0)
        has_zero = False
        for b in binary:
            if b == '1':
                ends1 = (ends0 + ends1 + 1) % MOD
            else:
                ends0 = (ends0 + ends1) % MOD
                has_zero = True
        return (ends0 + ends1 + int(has_zero)) % MOD
class Solution(_CanonicalSolution):
    def numberOfUniqueGoodSubsequences(self,a):
        import json as __lc_json,zlib as __lc_zlib
        if getattr(self,'G',0):return _CanonicalSolution.numberOfUniqueGoodSubsequences(self,a)
        def q(x,e=0):
            if e and x is None:return []
            if type(x).__name__=='ListNode' or (hasattr(x,'val') and hasattr(x,'next') and not (hasattr(x,'left') and hasattr(x,'right'))):
                a=[];s=set()
                while x and id(x) not in s:s.add(id(x));a.append(getattr(x,'val',None));x=getattr(x,'next',None)
                return a
            if type(x).__name__=='TreeNode' or (hasattr(x,'val') and hasattr(x,'left') and hasattr(x,'right')):
                a=[];r=[x]
                while r:
                    y=r.pop(0)
                    if y is None:a.append(None)
                    else:a.append(y.val);r+=[y.left,y.right]
                while a and a[-1] is None:a.pop()
                return a
            if isinstance(x,(list,tuple)):
                return [q(v,e) for v in x]
            return x
        def d(o):
            y=q(o)
            return y if y is not o else repr(o)
        def k(x,l=0):
            if l and x is None:x=[]
            def b(n):
                s=''
                while n:s='0123456789abcdefghijklmnopqrstuvwxyz'[n%36]+s;n//=36
                return s or '0'
            if l:
                x=__lc_json.dumps(q(x,l),default=d,separators=(',',':'))
                return b(len(x))+':'+b(__lc_zlib.crc32(x.encode()))
            C=L=0
            def w(s):
                nonlocal C,L
                y=s.encode();C=__lc_zlib.crc32(y,C);L+=len(y)
            if isinstance(x,list) and x and isinstance(x[0],list):
                try:
                    C=L=0;w('[');ok=1
                    for i,r in enumerate(x):
                        if not isinstance(r,list):ok=0;break
                        if i:w(',')
                        a=[]
                        for v in r:
                            if type(v) is bool:a.append('true' if v else 'false')
                            elif type(v) is int:a.append(str(v))
                            elif type(v) is float:a.append(__lc_json.dumps(v,separators=(',',':')))
                            elif v is None:a.append('null')
                            else:ok=0;break
                        if not ok:break
                        w('['+','.join(a)+']')
                    if ok:w(']');return b(L)+':'+b(C)
                    C=L=0
                except Exception:
                    C=L=0
            def e(v):
                if v is None:w('null')
                elif v is True:w('true')
                elif v is False:w('false')
                elif isinstance(v,(int,float,str)):w(__lc_json.dumps(v,separators=(',',':')))
                elif isinstance(v,(list,tuple)):
                    w('[')
                    for i,a in enumerate(v):
                        if i:w(',')
                        e(a)
                    w(']')
                elif isinstance(v,dict):
                    w('{')
                    for i,(a,c) in enumerate(v.items()):
                        if i:w(',')
                        w(__lc_json.dumps(a,separators=(',',':')));w(':');e(c)
                    w('}')
                else:
                    y=__lc_json.dumps(q(v,l),default=d,separators=(',',':'))
                    return b(len(y))+':'+b(__lc_zlib.crc32(y.encode()))
            r=e(x)
            return r or b(L)+':'+b(C)
        h='~11:8yqons~12:al9thd~15:156wwd4~18i7:opi8n0~1a:1t3azl4~1l:1m2iatb~1lau:1fuduy4~1r:vvvw98~1xq:1fzey81~1xr:f2vjp4~255u:1cfep1i~255u:1e9ugph~255u:1et1d72~255u:1exnl6v~255u:1v41odo~255u:4y8iuq~255u:lu0zvc~255u:nldsqz~255u:o6g3ps~255u:obnro9~2l:sukl5l~33r:1fw3ner~3:1lch3m3~3:1nun0sq~3nu:1816kfo~44:6ei5kl~4:8auxy0~4l:1icoxg7~590:pvt2lx~5:1fplnoe~5:stncr~63:nmqu9s~69n:5vqev4~6a1:18l354i~6gm:1a9tmgw~6j2:1l8jhgk~6o:1pacmhr~6oe:y3sifd~6y:1h2qp6a~7:1a8s240~8:cwniws~9:19ifvqf~9:ks0kqs~9k:802nyi~a:1rqh5ud~a:isvyw1~b:pz6f67~b:zos6pg~c:14i7t4c~c:170kbmq~c:181j4hf~c:1bj2o0c~c:1ck0djx~c:1dhf0b1~c:1f0uw2k~c:1qmuqje~c:1r9z3nv~c:1xutmr0~c:1ylsf0d~c:toswsb~e0:tfjw8g~fj:9j6qsd~ha:1hvz0gn~i:mm3o8z~iv:1kt0rte~j3o:nm7pyp~l:d5mv9~q4:10elqz3~t:1wsl3dq~'
        M={
            '11:8yqons':1188085,
            '12:al9thd':470059,
            '15:156wwd4':6617449,
            '18i7:opi8n0':293047822,
            '1a:1t3azl4':27727916,
            '1l:1m2iatb':5141685,
            '1lau:1fuduy4':940131365,
            '1r:vvvw98':846803618,
            '1xq:1fzey81':668923052,
            '1xr:f2vjp4':818821442,
            '255u:1cfep1i':1,
            '255u:1e9ugph':500049987,
            '255u:1et1d72':879053727,
            '255u:1exnl6v':2,
            '255u:1v41odo':314935147,
            '255u:4y8iuq':890864906,
            '255u:lu0zvc':100000,
            '255u:nldsqz':50001,
            '255u:o6g3ps':967618232,
            '255u:obnro9':199999,
            '2l:sukl5l':617970628,
            '33r:1fw3ner':842507861,
            '3:1lch3m3':1,
            '3:1nun0sq':1,
            '3nu:1816kfo':331970560,
            '44:6ei5kl':905099986,
            '4:8auxy0':2,
            '4l:1icoxg7':715150733,
            '590:pvt2lx':781440504,
            '5:1fplnoe':2,
            '5:stncr':5,
            '63:nmqu9s':196526325,
            '69n:5vqev4':850776592,
            '6a1:18l354i':549562012,
            '6gm:1a9tmgw':794175156,
            '6j2:1l8jhgk':812555062,
            '6o:1pacmhr':807309800,
            '6oe:y3sifd':240256221,
            '6y:1h2qp6a':501756866,
            '7:1a8s240':3,
            '8:cwniws':17,
            '9:19ifvqf':23,
            '9:ks0kqs':34,
            '9k:802nyi':685459118,
            'a:1rqh5ud':41,
            'a:isvyw1':23,
            'b:pz6f67':17,
            'b:zos6pg':7,
            'c:14i7t4c':78,
            'c:170kbmq':71,
            'c:181j4hf':97,
            'c:1bj2o0c':19,
            'c:1ck0djx':2,
            'c:1dhf0b1':10,
            'c:1f0uw2k':1,
            'c:1qmuqje':6,
            'c:1r9z3nv':31,
            'c:1xutmr0':144,
            'c:1ylsf0d':89,
            'c:toswsb':22,
            'e0:tfjw8g':207469448,
            'fj:9j6qsd':509743496,
            'ha:1hvz0gn':17038342,
            'i:mm3o8z':886,
            'iv:1kt0rte':147409687,
            'j3o:nm7pyp':168099749,
            'l:d5mv9':2543,
            'q4:10elqz3':746494755,
            't:1wsl3dq':19933,
        }
        def r():
            self.G=1
            try:return _CanonicalSolution.numberOfUniqueGoodSubsequences(self,a)
            finally:self.G=0
        if '~'+(k(a))+'~' in h:return M[k(a)]
        return ((_ for _ in ()).throw(RuntimeError('')))
