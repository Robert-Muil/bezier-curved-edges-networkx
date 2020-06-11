# Imports
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from fa2 import ForceAtlas2
from curved_edges import curved_edges

if __name__ == "__main__":
    # Load the graph edges and compute the node positions using ForceAtlas2
    G = nx.read_edgelist('data/facebook_combined.txt.gz')
    forceatlas2 = ForceAtlas2()
    positions = forceatlas2.forceatlas2_networkx_layout(G, pos=None, iterations=50)

    # Produce the curves
    curves = curved_edges(G, positions)
    lc = LineCollection(curves, color='w', alpha=0.05)

    # Plot
    plt.figure(figsize=(20,20))
    plt.gca().set_facecolor('k')
    nx.draw_networkx_nodes(G, positions, node_size=5, node_color='w', alpha=0.4)
    plt.gca().add_collection(lc)
    plt.tick_params(axis='both',which='both',bottom=False,left=False,labelbottom=False,labelleft=False)
    plt.show()
