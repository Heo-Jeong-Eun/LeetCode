class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximun = max(nums)
        for i in range(len(nums)):
            if nums[i] == maximun:
                maxindex = i
            if nums[i] != maximun and maximun < 2*(nums[i]):
                return -1
        return maxindex