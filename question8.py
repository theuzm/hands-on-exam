def stepsToTheRight(nums, k):
    # Ensure k is within the range of the array's length
    k %= len(nums)
    # Rotating the array
    return nums[-k:] + nums[:-k]

nums = [1, 2, 3, 4, 5, 6, 7]
result = stepsToTheRight(nums, 3)
print(result)
