import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from fa2 import ForceAtlas2
from curved_edges import curved_edges

if __name__ == "__main__":
    # Concatenate seasons 1-7
    got_data = 'got-s{}-edges.csv'
    dfg = pd.DataFrame()
    for i in range(7):
        df_current = pd.read_csv(got_data.format(i+1),
                               names=['source','target','weight','season'],
                               skiprows=1)
        dfg = pd.concat([dfg, df_current])
    dfg.drop(['season'], axis=1, inplace=True)

    # Group by the edges so they are not duplicated
    dfgt = dfg.groupby(['source','target'], as_index=False).agg({'weight':'sum'})

    # Remove some outliers
    outliers = ['BLACK_JACK','KEGS','MULLY']
    dfgt = dfgt[~dfgt.source.isin(outliers)&~dfgt.target.isin(outliers)]

    # Load graph from pandas and calculate positions
    G = nx.from_pandas_edgelist(dfgt, source='source', target='target', edge_attr='weight')
    forceatlas2 = ForceAtlas2(edgeWeightInfluence=0)
    positions = forceatlas2.forceatlas2_networkx_layout(G, pos=None, iterations=1000)

    # Get curves
    curves = curved_edges(G, positions)

    # Make a matplotlib LineCollection - styled as you wish
    weights = np.array([x[2]['weight'] for x in G.edges(data=True)])
    widths = 0.5 * np.log(weights)
    lc = LineCollection(curves, color='w', alpha=0.25, linewidths=widths)

    # Plot
    plt.figure(figsize=(10,10))
    plt.gca().set_facecolor('k')
    nx.draw_networkx_nodes(G, positions, node_size=10, node_color='w', alpha=0.5)
    plt.gca().add_collection(lc)
    plt.tick_params(axis='both',which='both',bottom=False,left=False,labelbottom=False,labelleft=False)
    plt.show()