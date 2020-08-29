def make_ends(nums):
  result = []
  if len(nums) >= 2:
    result.append(nums[0])
    result.append(nums[-1])
    return result
  elif len(nums) == 1:
    result.append(nums[0])
    result.append(nums[0])
    return result
  return nums
