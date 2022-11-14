class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        answer = [num for num in nums if num != val]
        
        for i in range(len(answer)):
            nums[i] = answer[i]
        
        nums = nums[:len(answer)]
        
        return len(nums)