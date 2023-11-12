class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        route_nums = defaultdict(list)

        if source == target:
            return 0

        for i, route in enumerate(routes):
            if len(route) == 1:
                continue
            for node in route:
                route_nums[node].append(i)
        
        queue1, visited1 = deque(), set()   #from source
        queue2, visited2 = deque(), set()   #from target

        queue1.append(source)
        visited1.add(source)
        queue2.append(target)
        visited2.add(target)
        
        l = 0

        while queue1 and queue2:
            l += 1
            for _ in range(len(queue1)):
                curr= queue1.popleft()

                for route_num in route_nums[curr]:
                    for node in routes[route_num]:
                        if node in visited2:
                            return 2*l-1
                        elif node in visited1:
                            continue
                        else:
                            queue1.append(node)
                            visited1.add(node)


            for _ in range(len(queue2)):
                curr= queue2.popleft()

                for route_num in route_nums[curr]:
                    for node in routes[route_num]:
                        if node in visited1:
                            return 2*l
                        elif node in visited2:
                            continue
                        else:
                            queue2.append(node)
                            visited2.add(node)
            

        return -1