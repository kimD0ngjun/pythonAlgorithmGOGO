from collections import deque


class Solution(object):

    def isPalindrome(self, s):
        strs = deque(filter(lambda x: x.isalnum(), map(lambda x: x.lower(), s)))

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
        return True

        # arr=list(filter(lambda x:x.isalnum(), map(lambda x: x.lower(), s)))

        # arr = []
        # for i in s:
        #     if i.isalnum():
        #         arr.append(i.lower())
        # for i in range((len(arr) // 2)):
        #     if arr[i] != arr[-(i+1)]:
        #         return False
        # return True


sol = Solution()
result = sol.isPalindrome("A man, a plan, a canal: Panama")
print(result)

