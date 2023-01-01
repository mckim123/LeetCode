class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        target = s.split()
        p = list(pattern)
        if len(set(p)) != len(set(target)):
            return False
        substitution = dict()
        while p:
            letter = p.pop()
            next_answer = target.pop()
            if letter in substitution:
                if next_answer != substitution[letter]:
                    return False
            else:
                substitution[letter] = next_answer
        return not target