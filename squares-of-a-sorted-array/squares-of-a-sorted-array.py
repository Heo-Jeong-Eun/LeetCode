import math

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return list(sorted(pow(n, 2) for n in nums))