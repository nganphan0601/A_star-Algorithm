import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
def create_graph():
    G = nx.Graph()
    # Add nodes
    G.add_nodes_from(['Vancouver', 'North Vancouver', 'West Vancouver', 'Burnaby', 'Richmond', 'Surrey', 
             'New Westminster', 'Delta', 'Langley', 'Abbotsford', 'Chilliwack', 'Hope', 'Mission'])
    # Add edges
    G.add_edge('Vancouver', 'North Vancouver', weight=15.1)
    G.add_edge('Vancouver', 'West Vancouver', weight=12.1)
    G.add_edge('Vancouver', 'Burnaby', weight=11.6)
    G.add_edge('Vancouver', 'Richmond', weight=13.5)

    G.add_edge('Surrey', 'New Westminster', weight=7.1)
    G.add_edge('Surrey', 'Delta', weight=26.3)
    G.add_edge('Surrey', 'Langley', weight=18.7)

    G.add_edge('Burnaby', 'New Westminster', weight=7.1)
    G.add_edge('Burnaby', 'Richmond', weight=21.6)
    G.add_edge('Burnaby', 'North Vancouver', weight=18.3)

    G.add_edge('Richmond', 'Delta', weight=14.1)
    G.add_edge('Richmond', 'New Westminster', weight=22.5)

    G.add_edge('West Vancouver', 'North Vancouver', weight=7)

    G.add_edge('Langley', 'Abbotsford', weight=31.5)

    G.add_edge('Abbotsford', 'Mission', weight=18.5)
    G.add_edge('Abbotsford', 'Chilliwack', weight=36.8)

    G.add_edge('Mission', 'Hope', weight=81.1)
    G.add_edge('Mission', 'Chilliwack', weight=47.8)
    G.add_edge('Hope', 'Chilliwack', weight=52.4)

    return G

def draw_graph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='yellow', font_size=10, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()