class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        temp = []
        
        for i in arr:
            if i == 0:
                temp.append(i)
            temp.append(i)
            
        answer = temp[:len(arr)]
        
        for i in range(len(arr)):
            arr[i] = answer[i]
        