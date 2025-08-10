
def majorityElement(nums):
    # nums.sort()
    # n = len(nums)
    # return nums[n//2]

    n = len(nums)
    m = dict()
    for num in nums:
        m[num] += 1
    
    n = n//2

    for key,value in m.items():
        if value>n:
            return key
    return 0

majorityElement([1,2,2,3])