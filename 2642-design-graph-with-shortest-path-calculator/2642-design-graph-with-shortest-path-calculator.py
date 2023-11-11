class Graph:

    MAX = 10 ** 8
    
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph = [[Graph.MAX] * n for _ in range(n)]
        for edge in edges:
            self.graph[edge[0]][edge[1]] = edge[2]


    def addEdge(self, edge: List[int]) -> None:
        self.graph[edge[0]][edge[1]] = edge[2]
        

    def shortestPath(self, node1: int, node2: int) -> int:
        start = node1
        
        not_visited = set(range(self.n))
        
        to_visit = [(0, start)]
        while to_visit:
            d, curr = heapq.heappop(to_visit)
            if curr == node2:
                return d
            if curr not in not_visited:
                continue
            not_visited.remove(curr)
                
            nears = self.graph[curr]
            for near in not_visited:
                if nears[near] == Graph.MAX:
                    continue
                heapq.heappush(to_visit, (d + nears[near], near))
        
        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)