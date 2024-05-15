"""
로그에는 두 가지 유형이 있습니다:

문자 로그: 식별자를 제외한 모든 단어가 소문자 영어 문자로 구성됩니다.
숫자 로그: 모든 단어(식별자 제외)가 숫자로 구성됩니다.
이러한 로그를 다시 정렬합니다:

문자-로그가 모든 숫자-로그 앞에옵니다.
# 먼저 문자 종류인지 숫자 종류인지 순서 정리
# 아예 문자 배열과 숫자 배열로 나눠서 변수에 할당
# 문자열 인덱스 0부터 2까지의 값이 "dig"인지 "let"인지를 구별

문자 로그는 내용에 따라 사전순으로 정렬됩니다. 내용이 같으면 식별자를 기준으로 사전순으로 정렬합니다.
# 내용은 문자 로그든 숫자 로그든 인덱스 5부터 시작, 그냥 sorted 메소드를 쓰면 되려나

숫자 로그는 상대적인 순서를 유지합니다.
로그의 최종 순서를 반환합니다.
"""
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        strs = []
        nums = []

        # 문자 로그와 숫자 로그 나누기
        for log in logs:
            splited = log.split(maxsplit=1)

            if splited[1][0].isdigit():
                nums.append(splited)
            else:
                strs.append(splited)

        # 사전 순으로 재정렬
        # 아니 숫자는 상대적인 배열이면 걍 그대로 놔두라는 거네...?
        # sorted 람다식 문법 익히기(기준 순서)
        sorted_strs = sorted(strs, key=lambda s: (s[1], s[0]))

        print(sorted_strs)
        print(nums)

        result = [' '.join(inner_list) for inner_list in sorted_strs + nums]

        return result

s = Solution()
print(s.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))

"""
https://leetcode.com/problems/reorder-data-in-log-files/submissions/
"""