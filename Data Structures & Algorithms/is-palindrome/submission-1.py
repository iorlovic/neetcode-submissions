class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s is there but we need to delete non alphanumeric characters
        cleaned = "".join(c for c in s if c.isalnum())
        cleaned = cleaned.lower()
        cleaned_reversed = cleaned[::-1] # this is the pointer 

        #print(cleaned)
        #print(cleaned_reversed)

        for i in range(len(cleaned)):
            if cleaned[i] == cleaned_reversed[i]:
                continue
            else:
                return False
        return True