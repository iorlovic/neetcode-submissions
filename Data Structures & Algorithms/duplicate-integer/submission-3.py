class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = []

        for i in range(len(nums)):
            if nums[i] not in duplicates:
                duplicates.append(nums[i])
            else:
                return True
        return False
        