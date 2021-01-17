from grandalf.graphs import Vertex,Edge,Graph
import matplotlib.pyplot as plt
import networkx as nx

v1 = Vertex('Obavijest')
v2 = Vertex('Zaposlenik')
v3 = Vertex('Klijent')
v4 = Vertex('Recenzija')
v5 = Vertex('Poruka')
v6 = Vertex('Korisnik')
v7 = Vertex('FormaPrijava')
v8 = Vertex('Rezervacija')
v9 = Vertex('FormaGlavniMeni')
v10 = Vertex('Restoran')
v11 = Vertex('Lokacija')
v12 = Vertex('FormaRestoran')
v13 = Vertex('Piće')
v14 = Vertex('GaziranoPiće')
v15 = Vertex('NeGaziranoPiće')
v16 = Vertex('Hrana')
v17 = Vertex('HranaVečera')
v18 = Vertex('HranaDoručak')
v19 = Vertex('HranaRučak')

e1 = Edge(v1, v2)
e2 = Edge(v1, v5)
e3 = Edge(v4, v5)
e4 = Edge(v4, v3)
e5 = Edge(v2, v6)
e6 = Edge(v3, v6)
e7 = Edge(v6, v7)
e8 = Edge(v6, v9)
e9 = Edge(v6, v10)
e10 = Edge(v8, v6)
e11 = Edge(v10, v9)
e12 = Edge(v10, v12)
e13 = Edge(v11, v10)
e14 = Edge(v13, v10)
e15 = Edge(v14, v13)
e16 = Edge(v15, v13)
e17 = Edge(v16, v10)
e18 = Edge(v18, v16)
e19 = Edge(v19, v16)
e20 = Edge(v17, v16)

V = [v1 ,v2 ,v3 ,v4 ,v5 ,v6, v7, v8, v9, v10, v11, v12, v13, v14, v15, v16, v17, v18, v19]
E = [e1,e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15,e16, e17, e18, e19,e20]

g = Graph(V, E)

g.C

class defaultview(object):
    w,h = 10,10

for v in V: v.view = defaultview()

from grandalf.layouts import SugiyamaLayout

sug = SugiyamaLayout(g.C[0])
sug.init_all()
sug.draw()

dataX = []
dataY = []

for v in g.C[0].sV: 
    print("%s: (%d,%d)"%(v.data,v.view.xy[0],v.view.xy[1]))
    dataX.append(v.view.xy[0])
    dataY.append(v.view.xy[1])

plt.scatter(dataX, dataY)
plt.show()

# for l in sug.layers:
#     for n in l: print(n.view.xy,end='')
#     print('')

# for e,d in sug.ctrls.items():
#     print('long edge %s --> %s points:'%(e.v[0].data,e.v[1].data))
#     for r,v in d.items(): print("%s %s %s"%(v.view.xy,'at rank',r))