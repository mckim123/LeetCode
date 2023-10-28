class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = int(1e9) + 7
        
        if n==1 :
            return 5
        
        def mult(A, B):
            return [[sum(A[i][k] * B[k][j] for k in range(5)) % MOD for j in range(5)] for i in range(5)]

        def mat_pow(A, p):
            if p == 1:
                return A
            if p % 2:
                return mult(A, mat_pow(A, p-1))
            half_pow = mat_pow(A, p // 2)
            return mult(half_pow, half_pow)
        
        mat = [
            [0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0]
        ]
        
        return sum(sum(row) for row in mat_pow(mat, n-1)) % MOD
    
#         prev = [1, 1, 1, 1, 1]
        
#         for _ in range(n-1):
#             curr = []   # a, e, i, o, u
#             curr.append(prev[1])
#             curr.append((prev[0] + prev[2]) % MOD)
#             curr.append((prev[0] + prev[1] + prev[3] + prev[4]) % MOD)
#             curr.append((prev[2] + prev[4]) % MOD)
#             curr.append(prev[0])
#             prev = curr
            
#         return sum(prev) % MOD
        