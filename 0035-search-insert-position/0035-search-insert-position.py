class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        k=0
        for num in nums:
            if num < target:
                k += 1
            else: 
                break
        return k