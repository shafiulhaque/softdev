def first_last6(nums):
  return nums[0] == 6 or nums[len(nums)-1] == 6
 
def same_first_last(nums):
  return len(nums) >= 1 and nums[0] == nums[len(nums) -1]

def make_pi():
  pi = [3, 1, 4]
  return pi
 
def common_end(a, b):
  return a[0] == b[0] or a[len(a) -1] == b[len(b) - 1]

def sum3(nums):
  counter = 0
  for e in nums:
    counter += e
  return counter
 
def rotate_left3(nums):
  return [nums[1], nums[2], nums[0]]


