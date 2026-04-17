class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_array = sorted(nums)
        my_set = set(sorted_array)
        if len(sorted_array) != len(my_set):
            return True
        else:
            return False
