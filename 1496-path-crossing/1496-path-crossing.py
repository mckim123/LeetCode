class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        curr = [0, 0]
        visited.add(tuple(curr))
        for ch in path:
            if ch == "N":
                curr[0] += 1
            elif ch == "S":
                curr[0] -= 1
            elif ch == "E":
                curr[1] += 1
            else:
                curr[1] -= 1
            
            v = tuple(curr)
            if v in visited:
                return True
            visited.add(v)
        return False