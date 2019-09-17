class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mappings = {}
        indexForA = ord("a")
        for word in strs:
            wordId = [0] * 26
            for letter in word:
                wordId[ord(letter) - indexForA] += 1
            wordId = tuple(wordId)
            if wordId in mappings:
                mappings[wordId].append(word)
            else:
                mappings[wordId] = [word]
        ans = []
        for collections in mappings:
            ans.append(mappings[collections])
        return ans
