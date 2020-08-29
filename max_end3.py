def max_end3(nums):
  list1 = []
  list2 = []
  if nums[0] > nums[2]:
    for i in range(3):
      list1.append(nums[0])
    return list1
  else:
    for i in range(3):
      list2.append(nums[2])
    return list2
