class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = int(1e9) + 7
        
        prev = [1, 1, 1, 1, 1]
        
        for _ in range(n-1):
            curr = []   # a, e, i, o, u
            curr.append(prev[1])
            curr.append((prev[0] + prev[2]) % MOD)
            curr.append((prev[0] + prev[1] + prev[3] + prev[4]) % MOD)
            curr.append((prev[2] + prev[4]) % MOD)
            curr.append(prev[0])
            prev = curr
            
        return sum(prev) % MOD