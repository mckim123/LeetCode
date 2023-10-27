class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen = 0
        maxlr = [0, 0]
        n = len(s)
        
        for i, ch in enumerate(s):
            l, r = i-1, i+1
            
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            
            if maxlen < (r-l-1):
                maxlen = r-l-1
                maxlr = [l+1, r-1]
            
            l, r = i-1, i
            
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    break
                l -= 1
                r += 1
            
            if maxlen < (r-l-1):
                maxlen = r-l-1
                maxlr = [l+1, r-1]
            
        return s[maxlr[0]:maxlr[1]+1]
            
                
            