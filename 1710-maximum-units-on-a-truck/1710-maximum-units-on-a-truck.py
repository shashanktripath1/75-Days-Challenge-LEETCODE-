class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse=True)
        capacity=0
        for i in boxTypes:
            if i[0]<=truckSize:
                capacity+=i[0]*i[1]
                truckSize-=i[0]
            else:
                return capacity+(truckSize*i[1])
        return capacity
                
        
        