from typing import List

# 공간 복잡도 O(1)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 투 포인터 인덱스
        left = 0
        right = len(s) - 1

        while left < right:

            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            left += 1
            right -= 1


s = Solution()
s.reverseString(["h", "e", "l", "l", "o"])

"""
https://leetcode.com/problems/reverse-string/submissions/
"""