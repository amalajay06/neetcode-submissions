class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c=0
        seen=set()
        for i in nums:
            if i in seen:
                c+=1
            else:
                seen.add(i)
        if c>0:
            return True
        else:
            return False