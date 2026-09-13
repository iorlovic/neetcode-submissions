class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        req_length = nums * 2
        
        ans = nums *2

        # check size 
        if len(ans) == len(req_length):
            return ans
        else:
            print("ALERT")