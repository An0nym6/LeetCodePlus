class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []
        ans = []
        numWords = len(words)
        wordLen = len(words[0])
        for o in range(wordLen):
            parsedWords = []
            for i in range(o, len(s), wordLen):
                parsedWords.append(s[i:min(len(s), i + wordLen)])
            start = 0
            end = 0
            missing = words[:]
            while end < len(parsedWords):
                if parsedWords[end] in missing:
                    missing.remove(parsedWords[end])
                    end += 1
                    if not missing:
                        ans.append(o + start * wordLen)
                else:
                    while parsedWords[end] not in missing and start < end:
                        missing.append(parsedWords[start])
                        start += 1
                    if parsedWords[end] not in missing:
                        start += 1
                        end += 1
        return ans
