import os
import sys

# import gexf

from models.node import Node
from models.edge import Edge

INPUT_FILE_NAME = 'LesMiserables.gexf'

def read_and_format_data():
    """ Método para leitura do grafo """
    nodes = []
    edges = []
    graph = []

    with open(INPUT_FILE_NAME) as graph_file:
        graph = Gexf.importXML(graph_file)
    
    for node in graph.nodes.iteritems() : 
        nodes.append(Node(node.id, node.label))
        print(nodes)

    for edge in graph.edges.iteritems() : 
        edges.append(Edge(edge.id, edge.source, edge.target))
        print(edges)