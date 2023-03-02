class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        answer = True
        flag = True
        
        if len(arr) < 3:
            answer = False
        else:
            for i in range(len(arr) - 1):
                if arr[i] == arr[i + 1]:
                    answer = False
                    break
                elif arr[i] > arr[i + 1]:
                    if i == 0:
                        answer = False
                        break
                    else:
                        flag = False
                elif flag == False and arr[i] < arr[i + 1]:
                    answer = False
                    break
                elif i == len(arr) - 2 and flag:
                    answer = False
        return answer