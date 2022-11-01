import Counter from collections
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        return all(v < 4 for v in ((Counter(word1) - Counter(word2)) + (Counter(word2) - Counter(word1))).values())