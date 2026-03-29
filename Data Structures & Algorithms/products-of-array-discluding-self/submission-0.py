class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Get the length of the list
        len_list = len(nums)

        accumulator = 1
        i = 0
        j = 0
        result = []
        print(len_list)
        for _ in range(len_list * len_list): # nums x nums
            print(j)
            if j == (len_list - 1):
                # Finish
                if j != i:
                    accumulator *= nums[j]

                # Flush
                result.append(accumulator)

                # Reset
                accumulator = 1
                j = 0
                i += 1
            elif j != i:
                accumulator *= nums[j]
                j += 1
            else:
                j += 1 
        return result
        