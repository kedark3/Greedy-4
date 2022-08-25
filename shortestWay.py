# TC: :O(m+nlogk)where m is length of source n is length of target and k is avg no of indices in map list
# SC: O(n) https://leetcode.com/problems/shortest-way-to-form-string/submissions/
from bisect import bisect_left

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        sl = len(source)
        tl = len(target)
        
        count = 1
        
        indexMap = {}
        
        for i in range(sl):
            c = source[i]
            if c not in indexMap:
                indexMap[c] = []
            indexMap[c].append(i)
        
        tp = sp = 0
        while tp < tl:
            tchar = target[tp]
            if tchar not in indexMap:
                return -1
            indexli = indexMap[tchar]
            k = bisect_left(indexli, sp) # binary search
            if k < 0:
                k = -k-1
            if k == len(indexli):
                count+=1
                sp = 0
            else:
                sp = indexli[k]
                tp += 1
                sp += 1
            
        return count