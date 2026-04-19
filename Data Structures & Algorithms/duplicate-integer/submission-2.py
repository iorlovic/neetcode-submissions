class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenHash = set()

        for num in nums:
            if num in seenHash:
                return True
            seenHash.add(num)
        return False
            
