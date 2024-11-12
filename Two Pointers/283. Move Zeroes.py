def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    lastNonZero = 0

    for i in range(len(nums)):
        if nums[i] !=0:
            nums[lastNonZero] = nums[i]
            lastNonZero += 1

    for i in range(lastNonZero, len(nums)):
        nums[i] = 0


nums = [0,1,0,3,12]
moveZeroes(nums)
print(nums)