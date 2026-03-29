class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers) - 1

        for i in range(len(numbers)):
            if left >= right:
                return False

            sum_total = numbers[left] + numbers[right] 
            if sum_total == target:
                return [left + 1, right + 1]
            elif sum_total > target:
                right -= 1
            else:
                left += 1
        return False

