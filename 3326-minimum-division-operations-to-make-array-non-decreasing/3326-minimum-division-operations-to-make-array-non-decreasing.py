class Solution:
    def minOperations(self, nums: List[int]) -> int:
        primes = []
        for n in range(2, 1000):
            ok = True
            for p in primes:
                if n % p == 0:
                    ok = False
                    break
                if n // p < p:
                    break
            if ok:
                primes.append(n)
        
        ps = []
        for num in nums:
            val = num
            for p in primes:
                if num % p == 0:
                    val = p
                    break
                if num // p < p:
                    break
            ps.append(val)
        
        ans = 0
        ps.reverse()
        nums.reverse()
                
        prev = nums[0]
    
        
        for i in range(len(nums)):
            if prev < nums[i]:
                ans += 1
                if prev < ps[i]:
                    return -1
                prev = ps[i]
            else:
                prev = nums[i]
        return ans