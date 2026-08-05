class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seenHash = set()

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                #if i in seenHash:
                #    return True
                #seenHash.add(i)
                if nums[i] == nums[j] and abs(i-j)<= k:
                    return True
                
        return False