# import collections
# import re
# from typing import List
#
#
# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
#             .lower().split()
#                  if word not in banned]
#
#         counts = collections.Counter(words)
#         return counts.most_common(1)[0][0]

import collections
import re
from typing import List
from collections import Counter

#먼저 소문자 변환, 벤 리스트 대신 집합 사용으로 O(n)에서 O(1)로 개선
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        paragraph = paragraph.lower()
        words = re.sub(r'[^\w\s]', ' ', paragraph).split()

        banned_set = set(banned)
        counts = Counter()

        for word in words:
            if word not in banned_set:
                counts[word] += 1

        return counts.most_common(1)[0][0]