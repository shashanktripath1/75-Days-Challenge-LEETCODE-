class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        
        def combination(idx, target, path):
            if target < 0:
                return 
            
            if target == 0:
                result.append(path)
                return
                
            if idx == len(candidates):
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                combination(i + 1, target - candidates[i], path + [candidates[i]])
            
            
            
        combination(0, target, [])
        return result