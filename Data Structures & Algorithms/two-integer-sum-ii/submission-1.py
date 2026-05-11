class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        r = n - 1
        l = 0

        while l < r:
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r -= 1
            
            elif curSum < target:
                l += 1

            else:
                return [l + 1, r + 1]
        return[]

        