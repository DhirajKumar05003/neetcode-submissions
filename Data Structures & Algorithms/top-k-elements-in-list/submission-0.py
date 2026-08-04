from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frq=Counter(nums)
        res=[]
        for ke, v in frq.items():

            res.append([v,ke])
        res.sort()

        arr=[]
        while len(arr)<k:
            arr.append(res.pop()[1])

        return arr