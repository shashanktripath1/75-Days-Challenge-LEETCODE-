class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        cnt1,cnt2=0,0
        ele1,ele2=float('-inf'),float('-inf')
        for i in range(n):
            if cnt1==0 and nums[i]!=ele2:
                cnt1=1
                ele1=nums[i]
            elif cnt2==0 and nums[i]!=ele1:
                cnt2=1
                ele2=nums[i]
            elif nums[i]==ele1:
                cnt1+=1
            elif nums[i]==ele2:
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        cnt1,cnt2=0,0
        ans=[]
        for i in range(n):
            if nums[i]==ele1:
                cnt1+=1
            elif nums[i]==ele2:
                cnt2+=1
        check=int(n/3)+1
        if cnt1>=check:
            ans.append(ele1)
        if cnt2>=check:
            ans.append(ele2)
        return ans