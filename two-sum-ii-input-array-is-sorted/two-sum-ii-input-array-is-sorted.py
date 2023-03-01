import bisect
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i,num in enumerate(numbers):
            expected = target - num
            ind = bisect.bisect_left(numbers,expected,i+1)
            if ind < len(numbers) and numbers[ind] == expected:
                return [i+1,ind+1]
            