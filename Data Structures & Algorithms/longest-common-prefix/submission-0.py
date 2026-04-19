class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        prefix = ""

        for letters in zip(*strs):
            if len(set(letters)) == 1:
                prefix += letters[0]
            else:
                break


        return prefix

        