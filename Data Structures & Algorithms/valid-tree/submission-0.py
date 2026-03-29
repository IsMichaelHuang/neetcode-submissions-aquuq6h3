class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        hashSet = {i:[] for i in range(n)}
        for src, dist in edges:
            hashSet[src].append(dist)
            hashSet[dist].append(src)
        
        visit = set()
        def dfs(node, prevNode) -> bool:
            if node in visit:
                return False     
        
            visit.add(node)
            for neighbor in hashSet[node]:
                if neighbor == prevNode:
                    continue
                if not dfs(neighbor, node): return False
            return True

        return dfs(0, -1) and n == len(visit)


        