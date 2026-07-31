class NumArray:
    def __init__(self, nums):
        self.prefix = []
        cur = 0
        for n in nums:
            cur += n
            self.prefix.append(cur)

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefix[right]
        leftSum = self.prefix[left - 1] if left > 0 else 0
        return rightSum - leftSum

nums = [1, 2, 3, 4, 5]

obj = NumArray(nums)

print(obj.sumRange(1, 3))   # 9
print(obj.sumRange(0, 2))   # 6
print(obj.sumRange(2, 4))   # 12