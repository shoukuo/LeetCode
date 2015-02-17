def exch(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp
    
def QuickSort3Way(A, lo, hi):
    if lo >= hi:
        return 
    lt = lo
    gt = hi
    i = lo+1
    v = A[lo]
    while i <= gt:
        if A[i] > v:
            exch(A, i, gt)
            gt -= 1
        elif A[i] < v:
            exch(A, i, lt)
            i += 1
            lt += 1
        else:
            i += 1
    QuickSort3Way(A, lo, lt-1)
    QuickSort3Way(A, gt+1, hi)
    