class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.total =sum(self.nums)
        
    def update(self, index: int, val: int) -> None:
        n = self.nums[index] 
        self.nums[index] = val
        self.total = self.total - n + val
            
        
    def sumRange(self, left: int, right: int) -> int:
        n1 = sum(self.nums[0:left])
        n2 = sum(self.nums[right+1:])
        return  self.total -n1-n2