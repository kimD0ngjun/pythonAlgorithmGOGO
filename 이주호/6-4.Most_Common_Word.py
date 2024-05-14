import collections
import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        """
        import re 대체 단어가아닌 문자 공백으로 대체 후 소문자화와 분리 r의 경우에는 원시문자열을 의미.
        """


        clean_paragraph = re.sub(r'[^\w]',' ',paragraph)
        paragraph_lower = clean_paragraph.lower()
        words_list = paragraph_lower.split()

        words = []
        for word in words_list:
            if word not in banned:
                words.append(word)
        print(words)

        # words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
        # .lower().split() if word not in banned]
        #
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]

print(Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.",["hit"]))
