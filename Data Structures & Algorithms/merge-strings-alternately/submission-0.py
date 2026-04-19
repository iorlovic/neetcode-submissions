class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""

        minLen = len(word1)
        if len(word1) > len(word2):
            minLen = len(word2)

        for i in range(0, minLen):
            output += (word1[i])
            output += (word2[i])

        output += (word1[minLen:])
        output += (word2[minLen:])

        return(str(output))