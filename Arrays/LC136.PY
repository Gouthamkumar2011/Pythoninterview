def singleNumber(nums):
        freq={}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        for num,count in freq.items():
            if count == 1:
                return num

print(singleNumber([4,1,2,1,2]))
