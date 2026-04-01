class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)
        sameList = set()
        seq = 0
        res = []
        for i in s:
            if i in count:
                sameList.add(i)
                seq += 1
                count[i] -= 1
            
            if not count[i]:
                sameList.remove(i)

            if len(sameList) == 0:
                res.append(seq) 
                seq = 0
    
        return res
        