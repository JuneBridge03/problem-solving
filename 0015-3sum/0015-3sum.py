class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        SIZE = len(nums)

        nums.sort()
        # -4 -1 -1 0 1 2

        answers = []

        numsWithIndex = enumerate(nums)

        for i, e in numsWithIndex:
            if e > 0:
                break
            if e == 0:
                if i + 2 < SIZE and nums[i + 1] == 0 and nums[i + 2] == 0:
                    answers.append([0,0,0])
                break
            
            if i > 0 and e == nums[i - 1]:
                continue
            
            start = i + 1
            end = SIZE - 1

            beforeStart = None
            beforeEnd = None

            while start < end:
                if e + nums[start] + nums[end] == 0 and beforeStart != nums[start] and beforeEnd != nums[end]:
                    answers.append([e, nums[start], nums[end]])
                    beforeStart = nums[start]
                    beforeEnd = nums[end]
                    start += 1
                    end -= 1
                    continue

                if e + nums[start] + nums[end] >= 0:
                    end -= 1
                else:
                    start += 1
        
        return answers