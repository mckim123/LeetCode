class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        s = list(s)
        to_remove = len(s) - k
        max_letter_remove = s.count(letter) - repetition
        res = []

        for ch in s:
            while res and ch < res[-1]:
                if to_remove and (max_letter_remove or res[-1] != letter):
                    to_remove -= 1
                    if res.pop() == letter:
                        max_letter_remove -= 1
                else:
                    break
            res.append(ch)
        print(res)
        ans = []

        while to_remove:
            ch = res.pop()
            if ch == letter:
                max_letter_remove -= 1

                if max_letter_remove >= 0:
                    to_remove -= 1
            else:
                to_remove -= 1

        res.append(letter * max(0, -max_letter_remove))
        return "".join(res)