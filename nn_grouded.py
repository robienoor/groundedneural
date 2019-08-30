import numpy as np
from itertools import chain, combinations

def generateGraphs(noNodes):
    noEdges = noNodes * noNodes
    s = list(range(0,noEdges))
    powerset = list(chain.from_iterable(combinations(s,r) for r in range(len(s)+1)))

    return powerset

def main():

    noNodes = 3 

    powerset = generateGraphs(noNodes)

    print(powerset)
    print(len(powerset))



if __name__ == "__main__":
    main()