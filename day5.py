class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self,a):
        pvalue=0
        nvalue=0
        
        for num in a:
            if num>0:
                pvalue+=1
            elif num<0:
                nvalue+=1
        
        return[pvalue, nvalue]
