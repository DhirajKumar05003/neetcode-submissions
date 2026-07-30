class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequencys={}
        frequencyt={}
        for char in sorted(s):
            if char in frequencys:
                frequencys[char]+=1
            else:
                frequencys[char]=1
        for char in sorted(t):
        
            if char in frequencyt:
                frequencyt[char]+=1
            else:
                frequencyt[char]=1
        if frequencyt ==frequencys:
            return True
        return False
        
