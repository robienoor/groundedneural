import numpy as np
from itertools import chain, combinations

def generateGraphs(noNodes):
    noEdges = noNodes * noNodes
    s = list(range(0,noEdges))
    powerset = list(chain.from_iterable(combinations(s,r) for r in range(len(s)+1)))

    return powerset

def convertVectorToMatrixGraph(vectorGraph, noNodes):
    return vectorGraph.reshape((noNodes, noNodes))

def main():

    noNodes = 3 

    powerset = generateGraphs(noNodes)
    graphs = []

    for indices in powerset:
        graph =  np.zeros((noNodes*noNodes))
        graph[list(indices)] = 1
        graphs.append(graph)


    print(graphs[-2:])
    print(len(powerset))



if __name__ == "__main__":
    main()