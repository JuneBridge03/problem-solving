class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.getIndex(nums, target)

    def getIndex(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] < target:
                return 1
            else:
                return 0
        
        mid = len(nums) // 2
        if nums[mid] > target:
            return self.getIndex(nums[:mid], target)
        elif nums[mid] == target:
            return mid
        else:
            return mid + self.getIndex(nums[mid:], target)