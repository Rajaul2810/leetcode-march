from itertools import permutations
from math import factorial as f
def permutation(n, k):

    l = list(permutations(range(1, n+1)))
    b = ''
    for i,v in enumerate(l):
        if i == k-1:
            for j in v:
                b += str(j)
    return b




print(permutation(4,9))