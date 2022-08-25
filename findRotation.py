# TC :O(n)
# SC :constant
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        def findRotation(candidate):
            n = len(tops)
            topRes = 0 
            bottomRes = 0
            for i in range(n):
                if tops[i] != candidate and bottoms[i] != candidate:
                    return -1
                if (tops[i] != candidate) :
                     topRes +=1
                if (bottoms[i] != candidate) :
                     bottomRes +=1
         
            return min(topRes, bottomRes);
            
        result = findRotation(tops[0])
        if result != -1:
            return result
        return findRotation(bottoms[0])