# def longestcommonprefix(strs):
#     res = ""
#     for i in range(len(strs[0])):
#         for s in strs:
#             if i == len(s) or s[i] != strs[0][i]:
#                 return res
#         res += strs[0][i]
#     return res 

# print(longestcommonprefix(["flower","flow","flight"]))


# def removeDuplicates(nums):
#     l=1
#     for r in range (1,len(nums)):
#         if nums[r] != nums[r-1]:
#             nums[l] = nums[r]
#             l+=1
#     return nums[:l]

# print(removeDuplicates([1,1,2]))


# def searchInsert ( nums, target):
#         l,r = 0, len(nums) - 1
#         while l<=r:
#             mid = (l+r) // 2

#             if target == nums[mid]:
#                 return mid
            
#             if target > nums[mid]:
#                 l = mid + 1
#             if target <nums[mid]:
#                 r = mid - 1
#         return l

# print(searchInsert([1,3,5,6], 2))


def plusOne(digits):
        for i in range (len(digits)-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            digits[i] = 0
        
        return [1] + digits

print(plusOne([9,9,9,9,9]))