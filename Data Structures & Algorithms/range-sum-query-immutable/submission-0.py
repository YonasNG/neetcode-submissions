class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        curSum = 0

        for num in nums:
            curSum += num
            self.prefix.append(curSum)
            
    def sumRange(self, left: int, right: int) -> int:
        leftsum = self.prefix[left - 1] if left > 0 else 0
        rightsum = self.prefix[right]

        return rightsum - leftsum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)