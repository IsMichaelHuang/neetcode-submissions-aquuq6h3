class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        hashSet = {i:[] for i in range(n)}
        for src, dist in edges:
            hashSet[src].append(dist)
            hashSet[dist].append(src)

        visit = set()
        def dfs(node): 
            if hashSet[node] == []:
                return
                
            visit.add(node)
            for nei in hashSet[node]:
                if nei in visit:
                    continue
                dfs(nei)
            hashSet[node] = []
        
        res = 0
        for i in range(n):
            if i not in visit:
                dfs(i)
                res += 1
        return res
            
        