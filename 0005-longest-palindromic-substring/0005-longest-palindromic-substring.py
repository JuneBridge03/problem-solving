class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        answer = ''
        answerLength = 0
        
        start = 0
        end = 0
        while end < N:
            j = 0
            while start - j >= 0 and end + j < N:
                if s[start - j] != s[end + j]:
                    break
                j += 1
            
            j -= 1

            length = 2 * j + end - start + 1

            if answerLength < length:
                answer = s[start - j:end + j + 1]
                answerLength = length
            
            if end == start:
                end += 1
            else:
                start += 1
        
        return answer
