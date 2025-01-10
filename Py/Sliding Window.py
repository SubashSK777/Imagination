import math

maxSubArray

def maxSubArray(self, nums: List[int]) -> int:

  if len(nums) == 1:
      return nums[0]

  big_val = sum(nums)


  for k in range(len(nums)-1, -1, -1):
      inte_sum = -math.inf
      inte_sum = 0
      for i in range(k):
          inte_sum += nums[i]

      big_val = max(big_val, inte_sum)

      for j in range(k, len(nums)):
          inte_sum -= nums[j-k]
          inte_sum += nums[j]

          big_val = max(big_val, inte_sum)

  return big_val




          



