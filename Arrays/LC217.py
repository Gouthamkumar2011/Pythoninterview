def hasDuplicate(nums):
    freq={}
    for num in nums:
        if num in freq:
            freq[num] +=1
        else:
            freq[num] = 1
    
    for num,count in freq.items():
        if count >= 2:
            return True
    return False


print(hasDuplicate([1,2,2,2,5,6,5]))


