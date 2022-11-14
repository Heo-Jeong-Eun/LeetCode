class Solution:
    def reverseWords(self, s: str) -> str:
        split_str = s.split()
        
        for i in range(len(split_str)):
            split_str[i] = split_str[i][::-1]
            
        return ' '.join(split_str)