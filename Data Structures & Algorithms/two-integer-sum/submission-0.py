class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()

        for x in range(len(nums)):
            found = target - nums[x]
            
            if found not in seen:
                seen[nums[x]] = x
            else: 
                return [seen[found], x]
                


3,0
4,1




