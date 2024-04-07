class Solution:
    def checkValidString(self, s: str) -> bool:
        c = [0] * 3
        for ch in s:
            if ch == "(":
                c[0] += 1
            elif ch == ")":
                c[1] += 1
            else:
                c[2] += 1
        
        if abs(c[0] - c[1]) > c[2]:
            return False
        
        o1 = (c[2] + c[1] - c[0]) // 2
        c1 = (c[2] + c[0] - c[1]) // 2
        c2 = c[2] - c1
        
        cur = 0
        i = 0
        for ch in s:
            if ch == "(":
                cur += 1
            elif ch == ")":
                cur -= 1
                if cur < 0:
                    return False
            else:
                if i < o1:
                    cur += 1
                elif i >= c2:
                    print("i=",i)
                    cur -= 1
                    if cur < 0:
                        return False
                i += 1
        
        return True
            
