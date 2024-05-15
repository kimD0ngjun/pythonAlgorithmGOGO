from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = defaultdict(list)
        # 자바의 Map 인터페이스, 존재하지 않는 키 에러 방지

        for word in strs:
            rearrangedWord = self.rearrangeString(word)
            check[rearrangedWord].append(word)
            # 만약 rearrangedWord라는 키가 이미 존재하면
            # 해당 키에 대한 값인 리스트에 새로운 단어를 추가

        return list(check.values())

    def rearrangeString(self, input):
        sorted_chars = sorted(input)
        return ''.join(sorted_chars)