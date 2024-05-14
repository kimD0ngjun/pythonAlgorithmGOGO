from typing import List
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        # 문장 부호들 전부 제거
        # remove = "!?',;."
        # removed_str = ''.join(char for char in paragraph if char not in remove)
        removed_str = (paragraph
                       .replace('!', ' ')
                       .replace('?', ' ')
                       .replace(';', ' ')
                       .replace(',', ' ')
                       .replace('.', ' ')
                       .replace('\'', ' ')
                       .lower())
        # print(removed_str)

        # 단어들 전부 소문자화
        # str_list = removed_str.lower().split()
        str_list = re.split(r'\s+', removed_str.strip())
        banned_list = list(map(lambda x: x.lower(), banned))
        # print(str_list)
        # print(banned_list)

        # 리스트 컴프리헨션으로 금지 단어들 걸러내기
        for ban in banned_list:
            str_list = [x for x in str_list if x != ban]
        # print(str_list)

        # 딕셔너리로 단어들 카운팅
        count = {}

        for str_value in str_list:
            if str_value in count:
                count[str_value] += 1
            else:
                count[str_value] = 1

        # print(count)
        # print(max(count, key=count.get))

        return max(count, key=count.get)



s = Solution()
s.mostCommonWord("..Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])

"""
https://leetcode.com/problems/most-common-word/submissions/
"""