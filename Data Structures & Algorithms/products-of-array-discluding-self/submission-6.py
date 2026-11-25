class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x=[]
        prod=1
        c=0
        for i in range(len(nums)):
           if nums[i]==0:
            c+=1
            continue
           prod*=nums[i]
        for i in range(len(nums)):
            if nums[i]!=0 and c==0:
                x.append(prod//nums[i]) 
            elif ((nums[i]!=0 and c>=1) or (nums[i]==0 and c>1)):
                x.append(0)
            else:
                x.append(prod)
        return x
