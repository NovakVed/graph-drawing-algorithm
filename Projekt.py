import grandalf
from grandalf.layouts import SugiyamaLayout
import networkx as nx
import matplotlib.pyplot as plt
import csv

G = nx.DiGraph() # Build your networkx graph here

filename = input("Napiši naziv datoteke koje želiš dodati: ")
with open(f"{filename}.csv") as file:
    reader = csv.reader(file)

    for row in reader:
        G.add_edge(row[0], row[1])

g = grandalf.utils.convert_nextworkx_graph_to_grandalf(G) # undocumented function

class defaultview(object):
    w,h = 10,10

for v in g.C[0].sV: v.view = defaultview()

sug = SugiyamaLayout(g.C[0])
sug.init_all() # roots=[V[0]])
sug.draw() # This is a bit of a misnomer, as grandalf doesn't actually come with any visualization methods. This method instead calculates positions

poses = {v.data: (v.view.xy[0], v.view.xy[1]) for v in g.C[0].sV} # Extracts the positions

nodesWithPosition = list(poses.values())
nodesWithPosition.sort(key=lambda x: x[1], reverse=True)

counter = -1
distance = 30
previousY = nodesWithPosition[0][1]
offsetedNodes = []
for node in nodesWithPosition:
    currentY = node[1]
    if currentY == previousY:
        counter += 1
    else:
        distance = 30
        counter = 0
        previousY = currentY
        offsetedNodes.append((node[0], node[1]+distance))
        continue
    
    if counter % 3 == 0:
        distance /= 2
    
    offsetedNodes.append((node[0], node[1]+distance))
    # node[1] += distance
# for pos in poses:

offsetedPoses = {}


for vertex, position in poses.items():
    for node in offsetedNodes:
        if node[0] == position[0]:
            offsetedPoses[vertex] = node
            break
    offsetedPoses[vertex] = position

nx.draw(G, pos=offsetedPoses, with_labels=True)
import matplotlib.pyplot as plt
plt.show()