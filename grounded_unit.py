import numpy as np 


class GroundedNeural:

    def __init__(self, nodes):
        self.nodes = nodes
        self.b = self.generateMaskWeights()
        self.w


    def generateMaskBiases(self):

        b = np.zeros((self.nodes, self.nodes*self.nodes))
        for i in range(self.nodes):
            blocks = list(range(i,self.nodes*self.nodes,self.nodes))

            b[i,blocks] = 1

        return b

    def generateMaskWeights(self):

        w = np.ones((self.nodes, self.nodes*self.nodes))
        for i in range(self.nodes):
            blocks = list(range(i,self.nodes*self.nodes,self.nodes))

            w[blocks, i] = 0

        return w

    def firstLayer(self, inputGraph):

        # This makes sure that unattacked arguments have 1 on their sum column
        attacked_sums = 1 - np.heaviside(np.sum(inputGraph, axis=0), 0)
        print('attacked_sums: ', attacked_sums)

        # Here 
        attacked_nodes = [inputGraph[i,:]*attacked_sums[i] for i in range(len(attacked_sums))] 

        print('attacked_nodes: ', attacked_nodes)

        defeated_nodes = np.sum(attacked_nodes, axis=0)

        print('defeated_nodes: ', defeated_nodes)

        print('mask_weights: ', self.w_m)

        masked_graph = np.dot(defeated_nodes, self.w_m)
        masked_graph = masked_graph.reshape((self.nodes, self.nodes))

        print('mask_graph : ', masked_graph)

        updated_graph = masked_graph + inputGraph

        print('final: ', updated_graph)

        return updated_graph

    def process(self, graph):
        return self.firstLayer(graph)


def main():
    graph = np.array([[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0]])

    no_nodes = 4

    groundednn_layer1 = GroundedNeural(no_nodes)
    groundednn_layer2 = GroundedNeural(no_nodes)
    groundednn_layer3 = GroundedNeural(no_nodes)

    groundednn_layer1_output = groundednn_layer1.process(graph)    
    groundednn_layer2_output = groundednn_layer2.process(groundednn_layer1_output)  
    groundednn_layer3_output = groundednn_layer3.process(groundednn_layer2_output)  

    return

if __name__ == "__main__":
    main()