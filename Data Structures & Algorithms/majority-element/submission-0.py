class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        counts = {}
        target = len(nums)/2

        for item in nums:
            counts[item] = counts.get(item, 0) + 1
            if counts[item] > target:
                return item
        