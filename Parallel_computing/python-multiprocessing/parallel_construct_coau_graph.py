import numpy as np
from datetime import datetime
from multiprocessing import Pool
import pandas as pd
import networkx as nx
import time

integ = pd.read_csv('/media/bentao/ecosystem_01/data/fromPKG/projs_pmid_aid.csv', header=None)
integ.rename(columns={0:'PMID', 1:'AID', 2:'CORE_PROJECT_NUM'}, inplace=True)
# Three columns corresponding to "PMID", "AID", "CORE_PROJECT_NUM"
print('data loaded ...')

# splitting

splitted = np.array_split(integ['CORE_PROJECT_NUM'].unique(), 5) # split it into 5 batches
batches = [list(ary) for ary in splitted]

# insert an element to each list for naming the list
num = 0
for bat in batches:
    bat.insert(0, str(num))
    num += 1


# input: a list of CORE_PROJECT_NUM
# output: networkx graph object G or write G into a local file
def coauthor_net(core_list):
    print('processing {}...'.format(core_list[0]))
    start = time.time()
    flag = 0
    write_path = '/media/bentao/ecosystem_01/data/coau_nets/'
    
    for core_proj in core_list:
        df = integ[integ['CORE_PROJECT_NUM'] == core_proj]
        df = df[['PMID','AID']]

        G = nx.Graph()
        pmid_indices = set(df['PMID'])

        for pmid in pmid_indices:
            paper_df = df[df['PMID'] == pmid]
            if paper_df.shape[0] < 2: # single author paper
                continue
            else:
                w = round((1 / paper_df.shape[0]), 4) # calculate the weight before removing authors with AID=0
                paper_df = paper_df[paper_df['AID'] != 0] # some authors could not be disambiguated
                
                authors = list(paper_df['AID'].unique())
                au_num = len(authors)
                if au_num == 0:
                    continue
                elif au_num == 1:
                    G.add_node(authors[0])
                else:
                    index_list = range(au_num)
                    for i in index_list:
                        j = i+1
                        while j in index_list:
                            nodea = authors[i]
                            nodeb = authors[j]
                            if G.has_edge(nodea, nodeb):
                                G[nodea][nodeb]['weight'] += w
                            else:
                                G.add_edge(nodea, nodeb, weight=w)
                            j += 1
        if len(G.nodes()) > 0:
            nx.write_graphml_lxml(G, write_path+'graphml/'+core_proj+'.graphml', encoding='utf-8', prettyprint=False)
            nx.write_pajek(G, write_path+'pajek/'+core_proj+'.net')

        flag += 1
        if flag % 500 == 0:
            end = time.time()
            print('pip {}: {}/{} constructed, time elapsed: {} mins, now is {}'.format(core_list[0],
                                                                                       flag,
                                                                                       len(core_list)-1,
                                                                                       round((end-start)/60,4),
                                                                                       datetime.now().strftime('%H:%M:%S')), end='\r')
    end = time.time()
    print('\n===pip {} finished at {}, total time: {} mins==='.format(core_list[0],
                                                              datetime.now().strftime('%H:%M:%S'),
                                                              round((end-start)/60,4)))

# start paralle processing
pool = Pool(5) # specify how many cpus allocated to this task
# this is memory consuming, so the optimazation to this parameter
# is about total_memory divided memory_needed_for_each_batch
with pool:
    pool.map(coauthor_net, batches)
    

# (anaconda3)bentao@BIL-WS8:/media/bentao/ecosystem_01$ python3 parallel_construct_coau_graph.py 
# data loaded ...
# processing 0...
# processing 1...
# processing 2...
# processing 3...
# processing 4...
# pip 4: 29500/29633 constructed, time elapsed: 761.7448 mins, now is 09:27:52
# ===pip 4 finished at 09:31:17, total time: 765.1625 mins===
# pip 3: 29500/29634 constructed, time elapsed: 767.1134 mins, now is 09:33:14
# ===pip 3 finished at 09:36:40, total time: 770.5468 mins===
# pip 2: 29500/29634 constructed, time elapsed: 778.2315 mins, now is 09:44:21
# ===pip 2 finished at 09:47:48, total time: 781.6708 mins===
# pip 1: 29500/29634 constructed, time elapsed: 805.3653 mins, now is 10:11:29
# ===pip 1 finished at 10:14:56, total time: 808.8055 mins===
# pip 0: 29500/29634 constructed, time elapsed: 952.7992 mins, now is 12:38:55
# ===pip 0 finished at 12:42:23, total time: 956.2538 mins===
# # It takes 14 hours to finish all parallel processes.
