class Solution:

    def encode(self, strs: List[str]) -> str:
        len_strs = []
        encoded_len = ''
        for s in strs:
            len_s = len(s)
            encoded_len += str(len_s) + '@'
            len_strs.append(str(len_s)) 
        result = encoded_len + '\u03A9' + ''.join(strs)
        return result

    def decode(self, s: str) -> List[str]:
        list_s = list(s)
        # Get the values before the delimiter
        decoded_len = []
        d_len = ''
        offset = 0 
        for c in list_s:
            if c == "\u03A9":
                offset += 1 # Account for the delimiter
                break
            if c != '@':
                d_len += c
            else:
                decoded_len.append(int(d_len)) 
                d_len = '' # Reset the accumulator
            offset += 1
        
        new_list_s = list_s[offset:]
        result = []
        previous_l = 0
        print(decoded_len)
        print(new_list_s)
        for l in decoded_len:
            word_list = new_list_s[previous_l:previous_l + l]
            previous_l += l
            result.append(''.join(word_list))
        return result

