class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = []

        #minLen = len(word1)
        #if len(word1) > len(word2):
        #    minLen = len(word2)

        minLen = min(len(word1), len(word2))

        for i in range(0, minLen):
            output.append(word1[i])
            output.append(word2[i])

        output.append(word1[minLen:])
        output.append(word2[minLen:])

        return "".join(output)