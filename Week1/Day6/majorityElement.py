class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else: 
                count[i] = 1
            
        for i in range(len(nums)):
            if count[nums[i]] > (len(nums)/2):
                return nums[i]
