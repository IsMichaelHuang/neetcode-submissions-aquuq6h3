class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            distance.append((dist, [x, y]))
        
        heapq.heapify(distance) 
        res = []
        for _ in range(k):
            res.append(heapq.heappop(distance)[1])
        
        return res