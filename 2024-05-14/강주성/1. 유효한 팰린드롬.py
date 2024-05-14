from collections import deque

#데크 이용
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True


#슬라이싱 이용
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        return strs == strs[::-1]



