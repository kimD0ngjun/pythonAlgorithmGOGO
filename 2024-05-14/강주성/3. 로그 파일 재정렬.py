from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits, letters = [],[]
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        # letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        def letters_sort(log):
            parts = log.split()
            a, b = parts[0], parts[1:]
            return (b,a)

        letters.sort(key=letters_sort)
        return letters + digits
