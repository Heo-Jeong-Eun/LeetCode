class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_dict = dict(Counter(nums))
        keys = nums_dict.keys()
        
        index = 0
        
        for i in range(3):
            if i in keys:
                for j in range(nums_dict[i]):
                    nums[index] = i
                    index += 1