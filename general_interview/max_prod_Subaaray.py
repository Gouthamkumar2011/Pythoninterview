class Solution:
    def maxProduct(self, nums):
        res = max(nums)
        curMin, curMax = 1,1

        for n in nums:
            if n==0:
                curMin,curMax = 1,1
                continue
            tmp = n*curMax
            curMax = max(n*curMax,n*curMin, n)
            curMin = min(tmp, n*curMin,n)
            res = max(res,curMax)
        return res

obj = Solution()
print(obj.maxProduct([1,2,3,-5]))