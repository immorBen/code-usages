import numpy as np
import networkx as nx
from datetime import datetime
from multiprocessing import Pool
from os import walk
import time
import pandas as pd


# step 1: get all files
path = '/media/usr/ecosystem_01/data/coau_nets/graphml/'
metrics_path = '/media/usr/ecosystem_01/data/net_metrics/'
for (root, dirs, all_files) in walk(path):
    break

files = [f.split('.')[0] for f in all_files]
# step 2: splitting
splitted = np.array_split(files, 5) # split it into 5 batches
batches = [list(ary) for ary in splitted]

# insert an element to each list for naming the list
num = 0
for bat in batches:
    bat.insert(0, str(num))
    num += 1


# define read-calculate operations for each batch
'''
E: number of edges
N: number of nodes

The average degree:
<k>= 2E/N (total edges/total nodes)

Density:
a measure of the prevalence of dyadic linkage or direct tie within a social network;
it is equal to the proportion of actual connections (edges) to potential connections (edges),
density = E / [n(n-1)/2]

:: Diameter and Distance require completely connected graphs.
'''

def read_graph(grap_name_list): 
    # input: contains a group of CORE_PROJECT_NUM, an example of them is 'C06AI058609'
    print('processing {} ...'.format(grap_name_list[0]))
    start = time.time()
    
    write_file = open(metrics_path+grap_name_list[0]+'batch.csv', 'w', encoding='utf-8')
    head = ['CORE_PROJECT_NUM', 'Nodes', 'Edges', 'Nodes_lcc', 'Edges_lcc',
            'avg_degree', 'avg_weighted_degree', 'density', 'avg_clus_coeff',
            'weighted_avg_clus_coeff\n']
    # lcc denotes largest connected component
    write_file.write(','.join(head))
    
    flag = 0
    for gra in grap_name_list[1:]:
        g = nx.read_graphml(path+gra+'.graphml')
        
        # number of edges, nodes
        n, e = g.number_of_nodes(), g.number_of_edges()
        
        # largest connected components
        ccp = nx.connected_components(g)
        largest_cc = max(ccp, key=len)
        s = g.subgraph(largest_cc).copy()
        nlcc, elcc = str(len(s.nodes())), str(len(s.edges()))
        
        # average degree & average weighted degree
        # https://networkx.org/documentation/stable/_modules/networkx/classes/function.html#density
        d = (deg for (node,deg) in nx.classes.function.degree(g))
        avg_deg = str(round(sum(d)/n, 4))
        wd = (deg for (node,deg) in nx.classes.function.degree(g, weight='weight'))
        avg_weigh_deg = str(round(sum(wd)/n, 4))
        
        # density
        dens = nx.classes.function.density(g)
        dens = str(round(dens,4))
        
        # average clustering coefficient, see documentation for details
        avg_cc = str(round(nx.average_clustering(g), 4))
        avg_weighted_cc = str(round(nx.average_clustering(g, weight='weight'), 4))
                        
        row = [gra, str(n), str(e), nlcc, elcc, avg_deg, avg_weigh_deg, dens, avg_cc, avg_weighted_cc+'\n']
        write_file.write(','.join(row))
        
        flag += 1
        if flag % 500 == 0:
            end = time.time()
            print('batch {}: {}/{} processed, time eplased: {} mins, current time: {}'.format(grap_name_list[0],
                                                                            flag, len(grap_name_list),
                                                                            round((end-start)/60, 4),
                                                                            datetime.now().strftime('%H:%M:%S')),
                                                                            end='\r')
            
    write_file.close()
    end = time.time()
    print('\n===batch {} spent {} mins, current time: {}==='.format(grap_name_list[0],
                                                              round((end-start)/60, 4),
                                                              datetime.now().strftime('%H:%M:%S')))


pool = Pool(5) 
with pool:
    pool.map(read_graph, batches)


print('calculating finished at: {}'.format(datetime.now().strftime('%H:%M:%S')))

# concatenate all outputs
metric_csvs = []
for (dirpath, dirname, filename) in walk(metrics_path):
    metric_csvs.extend(filename) # filename has a suffix '.graphml'
    break

candies = []
for csv in metric_csvs:
    data = pd.read_csv(metrics_path+csv)
    candies.append(data)
    
concated = pd.concat(candies)
concated.to_csv(metrics_path+'nets_metrics_merged.csv', index=False)

print('=== metrics concatenated ===')
