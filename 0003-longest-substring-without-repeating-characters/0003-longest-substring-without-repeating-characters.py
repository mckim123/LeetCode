class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_substring = ""
        max_length = 0
        curr_length = 0
        for i in range(len(s)):
            if s[i] not in curr_substring:
                curr_substring += s[i]
                curr_length += 1
                if curr_length > max_length:
                    max_length = curr_length
            else:
                curr_substring = curr_substring[curr_substring.index(s[i])+1:] + s[i]
                curr_length = len(curr_substring)
        return max_length