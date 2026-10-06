class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}

        for index, value in enumerate(nums):
            complement = target - value
            if complement in record:
                return [record[complement], index]
            record[value] = index
        



        
            
        


        



