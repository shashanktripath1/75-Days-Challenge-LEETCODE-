class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output=[]
        len_nums=len(nums)
        for x in range(0,len_nums-2):
            if x!=0 and nums[x]==nums[x-1]:
                continue
            lower=x+1
            higher=len_nums-1
            target=0-nums[x]
            
            while higher>lower:
                total=nums[lower]+nums[higher]
                
                if total==target:
                    output.append([nums[x],nums[lower],nums[higher]])
                    while higher>lower and nums[lower]==nums[lower+1]:
                        lower+=1
                
                    while higher>lower and nums[higher]==nums[higher-1]:
                        higher-=1
                    lower+=1
                    higher-=1
                    
                elif total>target:
                    higher-=1
                elif total<target:
                    lower+=1
        return output
        