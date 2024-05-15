import string

"""
유효한 팰린드롬 문제
투포인터 알고리즘 활용하기?
절반으로 자르고 뒷부분을 reverse 한 후, 겹치기? -> 시간복잡도는?
"""

# 문자열 길이가 짝수냐 홀수냐
"""
왼쪽 포인터의 인덱스 >= 오른쪽 포인터의 인덱스
... 가 될 때까지
while left < right:
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:

        """
        공백 최적화
        printable ASCII 판별 최적화
        """
        lower_s = ''.join(char for char in s if char not in string.punctuation and not char.isspace()).lower()

        # 투 포인터 인덱스
        left = 0
        right = len(lower_s) - 1

        while left < right:

            if lower_s[left] != lower_s[right]:
                return False

            left += 1
            right -= 1

        return True


s = Solution()
print(s.isPalindrome(" "))

"""
https://github.com/kimD0ngjun/backjoon_programmers/blob/main/LeetCode/Easy/0125-valid-palindrome/0125-valid-palindrome.py
"""