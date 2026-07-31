class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store=dict(enumerate(nums))
        reversed_dict = {v: k for k, v in store.items()}
        for i in range(len(nums)):
            if target - nums[i] in nums and i!=reversed_dict[target-nums[i]]:
                
                return [i,reversed_dict[target-nums[i]]]
            else: 
                continue
