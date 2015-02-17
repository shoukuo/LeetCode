class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        lo = 0
        hi = len(A)-1
        while True:
            p = self.partition(A, lo, hi)
            if (p > 0 and A[p] != A[p-1]) and (p < hi and A[p] != A[p+1]:
                r
    def partition(self, A, lo, hi):
        if lo >= hi:
            return
        lt = lo
        gt = hi
        i = lo+1
        v = A[lo]
        while i <= gt:
            if A[i] > v:
                self.exch(A, i, gt)
                i += 1
            elif A[i] < v:
                self.exch(A, i, lt)
                i += 1
                lt += 1
            else:
                i += 1        
    def sort(self, A, lo, hi):
        if lo >= hi:
            return
        lt = lo
        gt = hi
        i = lo+1
        v = A[lo]
        while i <= gt:
            if A[i] > v:
                self.exch(A, i, gt)
                i += 1
            elif A[i] < v:
                self.exch(A, i, lt)
                i += 1
                lt += 1
            else:
                i += 1
        self.sort(A, lo, lt-1)
        self.sort(A, gt+1, hi)
    
    def exch(self, A, i, j):
        tmp = A[i]
        A[i] = A[j]
        A[j] = tmp