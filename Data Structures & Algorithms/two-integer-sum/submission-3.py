class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1 = {}

        for i, num in enumerate(nums):
            hash1[num] = i
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash1 and hash1[diff] != i:
                return [i, hash1[diff]]
