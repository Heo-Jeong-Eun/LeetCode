class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result, cnt = 0, 0

        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                result = max(result, cnt)
                cnt = 0

        return max(result, cnt)
