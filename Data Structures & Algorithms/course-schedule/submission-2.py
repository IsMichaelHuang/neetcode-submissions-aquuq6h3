class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Adjecency list
        hashSet = {i:[] for i in range(numCourses)}
        for src, dist in prerequisites:
            hashSet[src].append(dist)
        
        visit = set()
        def dfs(node):
            if node in visit:
                return False

            if hashSet[node] == []:
                return True

            visit.add(node)
            for neighbor in hashSet[node]:
                if not dfs(neighbor): return False

            visit.remove(node)
            # Can complete
            hashSet[node] = []
            return True
                 
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
            
        