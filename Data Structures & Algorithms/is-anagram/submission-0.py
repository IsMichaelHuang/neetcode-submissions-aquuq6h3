class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       # Conditions:
        # Need to be the same lengths 
        # Same amount of chars

        len_s = len(s)
        len_t = len(t)

        if len_s != len_t:
            return False

        # Creating and sorting the list
        s_list = list(s)
        s_list.sort()
        
        t_list = list(t) 
        t_list.sort()

        for i in range(len_s):
            if s_list[i] != t_list[i]:
                return False
        return True
        
