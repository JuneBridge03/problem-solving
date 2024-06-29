class Solution:
    def trap(self, height: List[int]) -> int:
        SIZE = len(height)

        if SIZE == 1:
            return 0
        
        rightToLeft = []
        maximum = -1

        for e in height[::-1]:
            maximum = max(e, maximum)
            rightToLeft.append(maximum)
        
        rightToLeft = rightToLeft[::-1]

        answer = 0

        maximum = -1

        for index in range(SIZE):
            maximum = max(maximum, height[index])
            answer += (min(maximum, rightToLeft[index]) - height[index])
        
        return answer
