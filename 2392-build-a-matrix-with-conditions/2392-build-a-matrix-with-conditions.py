class Solution:
    def buildMatrix(self, k: int, rc: List[List[int]], cc: List[List[int]]) -> List[List[int]]:
        outs = [[] for _ in range(k)]
        ins = [0] * k
        d = set()
        for a, b in rc:
            if (a, b) in d:
                continue
            d.add((a, b))
            outs[a-1].append(b-1)
            ins[b-1] += 1
        s = []
        r1 = []
        for i in range(k):
            if not ins[i]:
                s.append(i)
        while s:
            c = s.pop()
            r1.append(c)
            for o in outs[c]:
                ins[o] -= 1
                if not ins[o]:
                    s.append(o)
        
        outs = [[] for _ in range(k)]
        ins = [0] * k
        d = set()
        for a, b in cc:
            if (a, b) in d:
                continue
            d.add((a, b))
            ins[b-1] += 1
            outs[a-1].append(b-1)
        s = []
        r2 = []
        for i in range(k):
            if not ins[i]:
                s.append(i)
        while s:
            c = s.pop()
            r2.append(c)
            for o in outs[c]:
                ins[o] -= 1
                if not ins[o]:
                    s.append(o)
        
        
        if len(r1) < k or len(r2) < k:
            return []
        
        r3 = [-1] * k
        for i in range(k):
            r3[r2[i]] = i
        
        
        ans = [[0] * k for _ in range(k)]
        for i in range(k):
            v = r1[i]
            ans[i][r3[v]] = v + 1
        return ans