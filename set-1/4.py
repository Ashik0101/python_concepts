
import math
""" Sum and list of numbres """

nums = [12, 44, 10, 11, 12, 300]
sum = 0
for i in range(len(nums)):
    sum += nums[i]
print("sum is :", sum)
average = sum/len(nums)
print('average is :', average)
print("floor value :", math.floor(average))
print("ceil value :", math.ceil(average))
print("rounded value :", round(average))
