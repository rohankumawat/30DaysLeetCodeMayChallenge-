class Solution:
    def findComplement(self, num: int) -> int:
        
        num = str(bin(num)[2:])
        
        num2 = ""
        
        for i in num:
            if i == "0":
                num2 += "1"
            else:
                num2 += "0"
            
        return int(num2,2)
