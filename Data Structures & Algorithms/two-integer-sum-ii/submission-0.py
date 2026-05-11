class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        r = n - 1
        l = 0

        for n in numbers:
            if numbers[l] + numbers[r] > target:
                l = l
                r = r - 1
            
            if numbers[l] + numbers[r] < target:
                l = l + 1
                r = r

            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]

        