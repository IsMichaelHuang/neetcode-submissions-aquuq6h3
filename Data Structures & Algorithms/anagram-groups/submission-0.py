from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Turn strings to list
        # Sort list of chars 
        # put sorted chars into new list
        freq_list = defaultdict(list) # Default an empty list
        for s in strs:
            sorted_str = "".join(sorted(s))
            freq_list[sorted_str].append(s)
        return list(freq_list.values())
        