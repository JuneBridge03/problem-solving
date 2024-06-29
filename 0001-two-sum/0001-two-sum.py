import collections

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numCnt = collections.defaultdict(int)

        minNum = None

        for e in list(set(nums)):
            minimum = min(e, target - e)
            numCnt[minimum] += 1
            if numCnt[minimum] == 2:
                minNum = minimum
                break
        
        if minNum == None:
            minNum = target // 2

        if minNum * 2 != target:
            return [nums.index(minNum), nums.index(target - minNum)]
        else:
            minIndex = nums.index(minNum)
            return [minIndex, nums[minIndex + 1:].index(minNum) + minIndex + 1]

