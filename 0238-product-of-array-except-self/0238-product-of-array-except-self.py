class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        SIZE = len(nums)

        rightToLeft = []

        mul = 1

        for e in nums[::-1]:
            mul *= e
            rightToLeft.append(mul)
        
        rightToLeft = rightToLeft[::-1]
        
        answer = []

        mul = 1

        for index in range(SIZE):
            if index > 0:
                mul *= nums[index - 1]
            a = mul
            if index + 1 < SIZE:
                a *= rightToLeft[index + 1]
            
            answer.append(a)
        
        return answer
