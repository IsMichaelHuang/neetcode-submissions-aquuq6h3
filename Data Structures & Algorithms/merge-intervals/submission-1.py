class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sIntervals = sorted(intervals, key=lambda x: x[0])
        print(sIntervals)

        res = []
        pInter = sIntervals[0]
        for i in range(1, len(sIntervals)):
            if pInter[1] < sIntervals[i][0]:
                res.append(pInter)
                pInter = sIntervals[i]
            else:
                pInter = [min(pInter[0], sIntervals[i][0]), max(pInter[1], sIntervals[i][1])]

        res.append(pInter) 
        return res

            
            
        