nums=[0,1,0,3,12]
l =0
r = len(nums)-1

if nums[l] ==0 & nums[r]!=0:
    nums[l],nums[r] = nums[r],nums[l]
print(nums)