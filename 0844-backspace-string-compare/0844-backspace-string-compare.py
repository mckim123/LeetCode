class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        end1, end2 = len(s), len(t)
        while end1 or end2:
            ch1, end1 = self.get_last_valid_character(s, end1)
            ch2, end2 = self.get_last_valid_character(t, end2)
            if ch1 != ch2:
                return False
        return True

    def get_last_valid_character(self, string, end):
        count = 0
        while end:
            ch = string[end-1]
            end -= 1
            if ch == "#":
                count += 1
            elif count:
                count -= 1
            else:
                return (ch, end)
        return ("", end)