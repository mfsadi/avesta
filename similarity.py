import difflib
from Levenshtein import distance


class similarity:
    def is_valid(self, word1, word2):
        diff = difflib.ndiff(word1, word2)
        for i in diff:
            if '- ' in i or '+ ' in i:
                i = i.replace('-', "").replace('+', "")
                if i == '  ':
                    return True
        return False

    def char_based_similarity(self, w1, w2, threshold=1):
        dist = distance(w1, w2)
        if dist == threshold:
            return self.is_valid(w1, w2)
        else:
            return False
