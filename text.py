import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt

# Zadavanje grafa
G = nx.DiGraph()

G.add_nodes_from(['Obavijest', 'Zaposlenik', 'Klijent', 'Recenzija',
'Poruka', 'Korisnik', 'FormaPrijava', 'Rezervacija', 'FormaGlavniMeni',
'Restoran', 'Lokacija', 'FormaRestoran', 'Piće', 'GaziranoPiće',
'NeGaziranoPiće', 'Hrana', 'HranaVečera', 'HranaDoručak', 'HranaRučak'])

G.add_edges_from([('Obavijest', 'Zaposlenik'), ('Obavijest', 'Poruka'), ('Recenzija', 'Poruka'),
('Recenzija', 'Klijent'), ('Zaposlenik', 'Korisnik'),('Klijent', 'Korisnik'), 
('Korisnik', 'FormaPrijava'),('Korisnik', 'FormaGlavniMeni'), ('Korisnik', 'Restoran'), 
('Rezervacija', 'Korisnik'), ('Restoran', 'FormaGlavniMeni'), ('Restoran', 'FormaRestoran'),
('Lokacija', 'Restoran'), ('Piće', 'Restoran'), ('NeGaziranoPiće', 'Piće'), ('GaziranoPiće', 'Piće'),
('Hrana', 'Restoran'), ('HranaVečera', 'Hrana'), ('HranaDoručak', 'Hrana'), ('HranaRučak', 'Hrana')])

# Nacrtan zadani graf u planarnom obliku
plt.title('Algoritmi za crtanje grafova')
nx.draw_planar(G, with_labels=True, arrows=True)
plt.show()


# Algoritam za crtanje hijerarhijski strukturiranog grafa
