def sum13(nums):
    """
    Step 0: Declare a sum and initialize it to 0
    Step 1: Inspect first element to see if it 13.
    Step 2: Loop through list and inspect element to see it is not 13.
    Step 3: Return sum
    """
    sum = 0


    if len(nums) > 0 and nums[0] != 13:  #to avoid list index out of range incase of empty list
        sum += nums[0]


    for i in range(1,len(nums),1):
        if nums[i] != 13 and nums[i-1] != 13:
            sum += nums[i]
    return sum

numlist = [1,2,3,4,5,12,13,4,1]
print(sum13(numlist))


