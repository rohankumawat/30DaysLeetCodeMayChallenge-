class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        num_sqrt = float(num ** 0.5) 
        
        if num_sqrt.is_integer() == True:
            return True
        else:
            return False
