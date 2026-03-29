class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def rootPar(node):
            res = node

            while res != par[res]:
                # path compression
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = rootPar(n1), rootPar(n2)

            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                par[p1] = p2
                rank[p1] += rank[p2]
            else:
                par[p2] = p1
                rank[p2] += rank[p1]
            return 1

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        return res
            
        