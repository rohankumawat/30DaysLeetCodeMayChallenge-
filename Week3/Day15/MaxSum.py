class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        K = self.Kadane(A)
        CS = 0
        for i in range(len(A)):
            CS += A[i]
            A[i] = -A[i]
        CS = CS + self.Kadane(A)
        
        if CS > K and CS != 0:
            return CS
        else:
            return K
        
    def Kadane(self, nums):
        cirsum, maxsum = nums[0], nums[0]
        for n in nums[1:]:
            cirsum = max(n, cirsum + n)
            maxsum = max(cirsum, maxsum)
        return maxsum
