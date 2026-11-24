class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        frequnet_dict = defaultdict(list)
        for s in strs:
            sorted_s = "".join(sorted(s))
            frequnet_dict[sorted_s].append(s)
        
        return list(frequnet_dict.values())

        