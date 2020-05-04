class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if ransomNote == '':
            return True
        elif magazine == '':
            return False
        elif len(ransomNote)>len(magazine):
            return False
        else:
            for i in ransomNote:
                if not i in magazine:
                    return False
                else:
                    magazine=magazine.replace(i,"",1)
            return True
