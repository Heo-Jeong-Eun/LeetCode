class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        answer = [0] * len(arr)
        answer[-1] = -1
        
        for i in range(len(arr) - 2, -1, -1): 
        # n - 2부터 0까지 가면서 index를 기준으로 오른쪽에 있는 elements 중 max를 구한다. 
            answer[i] = max([answer[i + 1], arr[i + 1]])
            
        return answer