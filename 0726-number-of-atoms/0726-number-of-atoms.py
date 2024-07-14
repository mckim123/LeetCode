class Solution:
    def countOfAtoms(self, f: str) -> str:
        a = [Counter()]
        i = 0
        while i < len(f):
            ch = f[i]
            if ch == "(":
                a.append(Counter())
                i += 1
            elif ch == ")":
                cnt = 0
                while i+1 < len(f) and f[i+1].isdigit():
                    i += 1
                    cnt = 10 * cnt + int(f[i])
                c = a.pop()
                cnt = max(cnt, 1)
                for k, v in c.items():
                    a[-1][k] += cnt * v
                i += 1
            else:
                k = ch
                cnt = 0
                i += 1
                while i < len(f):
                    ch1 = f[i]
                    if ch1.islower():
                        k += ch1
                        i += 1
                    elif ch1.isdigit():
                        cnt = cnt * 10 + int(ch1)
                        i += 1
                    else:
                        break
                cnt = max(1, cnt)
                a[-1][k] += cnt
        ans = []
        for k, v in a[-1].items():
            if v != 1:
                ans.append(k + str(v))
            else:
                ans.append(k)
        ans.sort()
        return "".join(ans)