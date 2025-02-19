class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
     
        t_index = 0
        
        for char in s:
            while t_index < len(t) and t[t_index] != char:
                t_index += 1
            
            if t_index == len(t):
                return False
            
            
            t_index += 1
        
       
        return True
