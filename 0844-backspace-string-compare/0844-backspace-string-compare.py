class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def convert(s):
            char_list = []
            for ch in s:
                if ch == "#":
                    if char_list:
                        char_list.pop()
                else:
                    char_list.append(ch)
            return char_list
        return convert(s) == convert(t)