class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_temp = set(range(1, len(nums) + 1))
        set_nums = set(nums)
        
        return list(set_temp - set_nums)