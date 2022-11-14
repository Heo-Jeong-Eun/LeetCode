class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        letf_sum = 0
        for i, x in enumerate(nums):
            if letf_sum == (total-letf_sum-x):
                return i
            letf_sum += x
        return -1

if __name__ == "__main__":
    nums = [1, 7, 3, 6, 5, 6]
    #nums = [-1, -1, -1, 0, 1, 1]
    sl = Solution().pivotIndex(nums)
    print(sl)