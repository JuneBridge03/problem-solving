from collections import deque

N = int(input())

nums = list(map(int, input().split()))

nums.sort()

def getAnswer(nums):

    A = deque([nums[N - 1]])

    isLittle = True

    little = 0
    big = N - 2

    for i in range(N - 1):
        if i % 4 <= 1:
            if i % 2 == 0:
                A.appendleft(nums[little])
            else:
                A.append(nums[little])
            little += 1
        else:
            if i % 2 == 0:
                A.appendleft(nums[big])
            else:
                A.append(nums[big])
            big -= 1
            
    answer = 0

    for i in range(N - 1):
        answer += abs(A[i] - A[i + 1])
    
    return answer


print(max(getAnswer(nums), getAnswer(nums[::-1])))