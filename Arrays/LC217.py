# def hasDuplicate(nums):
#     freq={}
#     for num in nums:
#         if num in freq:
#             freq[num] +=1
#         else:
#             freq[num] = 1
    
#     for num,count in freq.items():
#         if count >= 2:
#             return True
#     return False


# print(hasDuplicate([1,2,2,2,5,6,5]))

def hasDuplicate(nums):
        seen={}
        for num in nums:
            if num in seen:
                return True
            seen[num] = 1
        return False

print(hasDuplicate([1,2,2,2,5,6,5]))

