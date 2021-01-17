import networkx as nx
from networkx.algorithms.tree.recognition import is_tree
from networkx.drawing.nx_agraph import graphviz_layout
from graphviz import Digraph
import matplotlib.pyplot as plt
import csv
import sys

# Zadavanje grafa
G = nx.DiGraph()

# filename = input("Napiši naziv datoteke koje želiš dodati: ")
# with open(f"{filename}.csv") as file:

# testni input
with open('tablica.csv') as file:
    reader = csv.reader(file)

    for row in reader:
        G.add_edge(row[0], row[1])

# Nacrtan zadani graf u planarnom obliku
plt.title('Algoritmi za crtanje grafova')
nx.draw_planar(G, with_labels=True, arrows=True)
plt.show()

# Algoritam za crtanje hijerarhijski strukturiranog grafa

# Provjeri jeli graf aciklički
if nx.is_directed_acyclic_graph:
    print(f"Upisani graf je direktni aciklički graf (DAG)")
    if nx.check_planarity:
        print(f"Upisani graf je planaran")
        if is_tree:
            print(f"Stablo je")
    else:
        print(f"Upisani graf nije planaran")
        sys.exit()
        
# Promijeni što manje smjer bridova kako bi ga učinio cikličkim
else:
    print(f"Ne radi se o DAG grafu")
    sys.exit()

# Nacrtan hijerarhijski graf