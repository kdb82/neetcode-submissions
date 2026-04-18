class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        while nums:
            num = nums.pop(0)

            for n in nums:
                if n == num:
                    return True
        return False
        