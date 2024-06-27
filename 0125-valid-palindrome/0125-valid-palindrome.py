class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s) - 1
        while front < back:
            front_alpha = s[front]
            back_alpha = s[back]
            if not front_alpha.isalnum():
                front += 1
                continue
            if not back_alpha.isalnum():
                back -= 1
                continue
            
            if "A" <= front_alpha <= "Z":
                front_alpha = front_alpha.lower()
            if "A" <= back_alpha <= "Z":
                back_alpha = back_alpha.lower()
            
            if front_alpha == back_alpha:
                front += 1
                back -= 1
            else:
                return False
        return True
