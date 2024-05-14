class Solution:
    def longestPalindrome(self, s: str) -> str:
        group = []

        if len(s) <= 1:
            return s

        # 홀수 펠린드롬
        for i in range(len(s)):
            left = i
            right = i

            while left >= 0 and right <= len(s) - 1:
                if s[left] == s[right]:
                    group.append(s[left:right + 1])
                    left -= 1
                    right += 1
                else:
                    break

        # 짝수 펠린드롬
        for i in range(len(s)):
            left = i
            right = i + 1

            while left >= 0 and right <= len(s) - 1:
                if s[left] == s[right]:
                    group.append(s[left:right + 1])
                    left -= 1
                    right += 1
                else:
                    break

        return max(group, key=len, default="")