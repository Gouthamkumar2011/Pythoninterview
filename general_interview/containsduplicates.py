# #HASHSET
# def containsduplicates(nums):
#     hasset = set()
#     for n in nums:
#         if n in hasset:
#             return True
#         hasset.add(n)
#     return False
    
# containsduplicates([1,2,3,4,5,6,7,8])

#HASHMAP
def containsduplicate_1(nums):
    hashmap = {}
    for n in nums:
        if n in hashmap:
            return True
        hashmap[n] = hashmap.get(n,0) + 1
    return False

containsduplicate_1([1,2,3,4,5,6,7,8,7,9,1,2])